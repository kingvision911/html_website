import subprocess, time, re

def arp_protocal():
    result = subprocess.check_output("arp -a", shell=True)
    result = result.decode()
    out_put = re.findall("\d\d\d.*", str(result))
    out_put = out_put[1]
    out_put = out_put.split(" ")
    out_put = ' '.join(out_put)
    return out_put

if __name__ == "__main__":
    print("[+] Well Come to ARP-Spoof Detector...!")

result = arp_protocal()

try:
    while True:
        new_ip_test = subprocess.check_output("arp -a", shell=True)
        new_ip_test = new_ip_test.decode()

        if result in str(new_ip_test):
            time.sleep(2)
            print(f"\r[+] You are on {result}", end="")
        
        else:
            time.sleep(2)
            print('\n[-] You are under attack..!', end="")
except IndexError:
    print("\n[!] You are not connected to the internet...")

except KeyboardInterrupt:
    print("\n[!] Quiting the program... ")