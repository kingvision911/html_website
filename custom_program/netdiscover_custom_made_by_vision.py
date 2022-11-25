import scapy.all as scapy
import subprocess, re, argparse

try:
    def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", dest="interface", help="Type 'ifconfig' to see which interface has ip address.\n Examples \n     name_of_the_program [option] [interface]   \n The option is '-i' or '--interface' and the interface can be 'wlan0' or 'eth0'")
        options = parser.parse_args()
        return options


    def filter(interface):
        result = subprocess.check_output(["ifconfig", interface])
        found = re.findall("inet.*", str(result))
        for net in found:
            net = net.split(" ")
            net = net[1]
            net = net.split(".")
            net = net[0:3]
            net_answer = ".".join(net)
            net_answer += ".1/24"
            return net_answer


    def scan_ip(ip):
        arp_spoof = scapy.ARP(pdst=ip)
        broadcasting = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_spoof_broadcasting = broadcasting/arp_spoof
        answered = scapy.srp(arp_spoof_broadcasting, timeout=1, verbose=False)[0]

        big_list = []
        for elements in answered:
            small_dict = {"ip": elements[1].psrc, "mac": elements[1].hwsrc}
            big_list.append(small_dict)
            return big_list


    def print_something(result):
        print("__________________________________________\nIP\t\t\tMAC address\n------------------------------------------")
        try:
            for clients in result:
                print(clients["ip"] + "\t\t" + clients["mac"])
        except TypeError:
            print("[!] The interface you choose dose not have the ip \n    address or it is not connected to the internet.\n    Please choose another interface.")


    options = get_arguments()
    ip_range = filter(options.interface)
    scan_result = scan_ip(ip_range)
    print_something(scan_result)

except Exception:
    print("WARNING ! Use this program as a root. \n Type 'ifconfig' to see which interface has ip address.\n Examples \n     name_of_the_program [option] [interface]   \n The option is '-i' or '--interface' and the interface can be 'wlan0' or 'eth0'")