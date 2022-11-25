import subprocess, re

def systemcommand():
    ssid = subprocess.check_output(["nmcli", "connection", "show"])
    ssid = ssid.decode()
    ssid = re.findall("(.*\w\w\w\w\w\w\w\w)", ssid)
    for i in ssid:
        ssid = i.split("  ")
        ssid = ssid[0]
        print('\n')
        print(ssid)
        
        
        result = subprocess.check_output(["nmcli","--show-secrets", "connection","show", ssid])
        result = result.decode()
        password = re.findall("[^<.*](wireless-security.psk:(.*))", result)
        for value in password:
            for result in value:
                result = result.split(":")
                print(result[0])

systemcommand()
