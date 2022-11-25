import subprocess, smtplib, time, argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--ip', dest="ip", help="[-i] followed by the ip address you want to ping.")
    parser.add_argument('-b', '--ip1', dest="ip1")
    parser.add_argument('-c', '--ip2', dest="ip2")
    parser.add_argument('-d', '--ip3', dest="ip3")
    parser.add_argument('-e', '--ip4', dest="ip4")
    parser.add_argument('-f', '--ip5', dest="ip5")
    parser.add_argument('-g', '--ip6', dest="ip6")
    parser.add_argument('-i', '--ip7', dest="ip7")
    parser.add_argument('-j', '--ip8', dest="ip8")
    parser.add_argument('-k', '--ip9', dest="ip9")
    parser.add_argument('-l', '--ip10', dest="ip10")
    options = parser.parse_args()
    return options


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def ping_server(ip, ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, ip9, ip10):
    time_wait = 2
    try:
        while True:
            if ip:
                subprocess.call("ping -c 5 " + str(ip) + " > ping_output.txt", shell=True)
                result = subprocess.check_output("cat ping_output.txt", shell=True)
                result = result.decode()

                if "ttl=64 time" in result:
                    print(f"[+] [{ip}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip} can't be reached !")                   
            else:
                pass

            if ip1:
                subprocess.call("ping -c 5 " + str(ip1) + " > ping1_output.txt", shell=True)
                result1 = subprocess.check_output("cat ping1_output.txt", shell=True)
                result1 = result1.decode()

                if "ttl=64 time" in result1:
                    print(f"[+] [{ip1}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip1}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip1} can't be reached !")   
            else:
                pass

            
            if ip2:
                subprocess.call("ping -c 5 " + str(ip2) + " > ping2_output.txt", shell=True)
                result2 = subprocess.check_output("cat ping2_output.txt", shell=True)
                result2 = result2.decode()


                if "ttl=64 time" in result2:
                    print(f"[+] [{ip2}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip2}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip2} can't be reached !") 
            else:
                pass

            if ip3:
                subprocess.call("ping -c 5 " + str(ip3) + " > ping3_output.txt", shell=True)
                result3 = subprocess.check_output("cat ping3_output.txt", shell=True)
                result3 = result3.decode()

                if "ttl=64 time" in result3:
                    print(f"[+] [{ip3}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip3}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip3} can't be reached !")
            else:
                pass

            if ip4:
                subprocess.call("ping -c 5 " + str(ip4) + " > ping4_output.txt", shell=True)
                result4 = subprocess.check_output("cat ping4_output.txt", shell=True)
                result4 = result4.decode()


                if "ttl=64 time" in result4:
                    print(f"[+] [{ip4}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip4}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip4} can't be reached !")  
            else:
                pass

            if ip5:
                subprocess.call("ping -c 5 " + str(ip5) + " > ping5_output.txt", shell=True)
                result5 = subprocess.check_output("cat ping5_output.txt", shell=True)
                result5 = result5.decode()

                if "ttl=64 time" in result5:
                    print(f"[+] [{ip5}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip5}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip5} can't be reached !") 
            else:
                pass
            
            if ip6:
                subprocess.call("ping -c 5 " + str(ip6) + " > ping6_output.txt", shell=True)
                result6 = subprocess.check_output("cat ping6_output.txt", shell=True)
                result6 = result6.decode()

                if "ttl=64 time" in result6:
                    print(f"[+] [{ip6}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip6}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip6} can't be reached !") 
            else:
                pass

            if ip7:
                subprocess.call("ping -c 5 " + str(ip7) + " > ping7_output.txt", shell=True)
                result7 = subprocess.check_output("cat ping7_output.txt", shell=True)
                result7 = result7.decode()

                if "ttl=64 time" in result7:
                    print(f"[+] [{ip7}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip7}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip7} can't be reached !") 
            else:
                pass

            if ip8:
                subprocess.call("ping -c 5 " + str(ip8) + " > ping8_output.txt", shell=True)
                result8 = subprocess.check_output("cat ping8_output.txt", shell=True)
                result8 = result8.decode()

                if "ttl=64 time" in result8:
                    print(f"[+] [{ip8}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip8}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip8} can't be reached !") 
            else:
                pass

            if ip9:
                subprocess.call("ping -c 5 " + str(ip9) + " > ping9_output.txt", shell=True)
                result9 = subprocess.check_output("cat ping9_output.txt", shell=True)
                result9 = result9.decode()

                if "ttl=64 time" in result9:
                    print(f"[+] [{ip9}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip9}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip9} can't be reached !") 
            else:
                pass

            if ip10:
                subprocess.call("ping -c 5 " + str(ip10) + " > ping10_output.txt", shell=True)
                result10 = subprocess.check_output("cat ping10_output.txt", shell=True)
                result10 = result10.decode()

                if "ttl=64 time" in result10:
                    print(f"[+] [{ip10}] This server is reachebale.")

                else:
                    print(f"[-] You can't ping this server [{ip10}]!")
                    # send_mail("kingvision911@gmail.com", "VISION747489333", f"\n\n[+] The server with ip address {ip10} can't be reached !") 
                    time.sleep(time_wait)
            else:
                pass    

    except KeyboardInterrupt:
        print("[+] Quiting ..!")

    except OSError:
        print("[+] Error durring command execution.!")

options = get_arguments()
ping_server(options.ip, options.ip1, options.ip2, options.ip3, options.ip4, options.ip5, options.ip6, options.ip7, options.ip8, options.ip9, options.   ip10)       
