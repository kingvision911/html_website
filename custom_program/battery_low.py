#!/usr/bin/python3
import subprocess
import time
import os


def power_monitor():
    while True:
        power = subprocess.check_output("acpi", shell=True)
        power_converted = power.decode()
        power_list = power_converted.split(" ")
        percent = power_list[3]
        percent_try = ['20%,', '14%,', '8%,', '93%,']
        for percentage in percent_try:
            if percentage == percent:
                if "Dis" in power_converted:
                    os.system("mpg321 low-battery-sound.mp3")

        time.sleep(10)


power_monitor()
