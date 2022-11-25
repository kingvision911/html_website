import subprocess, time, smtplib


try:
    def send_mail(email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def ping_result():
        ip = input("IMPORTANT\n,"
                   "You can enter more than one ip address but remember to live a space between those ip\n,"
                   "Enter The Ip Address >> ")
        ip_add = ip.split(" ")
        time_wait = 30
        try:
            while True:
                for ip in ip_add:                
                    subprocess.call("ping -c 5 " + str(ip) + " > ping_output.txt", shell=True)
                    result = subprocess.check_output("cat ping_output.txt", shell=True)
                    result = result.decode()

                    if "ttl=64 time" in result:
                        print(f"[+] [{ip}] This server can be reached.")

                    else:
                        try:
                            print(f"[-] You can't ping this server [{ip}]!")
                            time_of_error = subprocess.check_output("date", shell=True)
                            time_of_error = time_of_error.decode()
                            send_mail("kingvision911@gmail.com", "VISION747489333", f"Subject: Server Tests.\n\n,"
                                                                                    f"[+] The server with ip address,"
                                                                                    f" [ {ip} ] can't be reached.,"
                                                                                    f" Time [ {time_of_error} ].")
                              
                        except OSError:
                            print("[+] Network is unreachable.")
                            continue                   
                print("\n")
                time.sleep(time_wait)

        except KeyboardInterrupt:
            print("[+] Quiting the program...!")

    ping_result()
except Exception as e:
    print(e)
    