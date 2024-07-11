#Sensor Service Check Version 1.0
#Owen Garland

#Check the statuses of all the services neccessary for sensor functionality
#Check through the logs for any errors.
#Check if the configurations are different and let the user know that they are and it could be wrong.

import os 
import subprocess

servicesList = ["rtk_bypassd.service", "suricata6.service", "rtk_zeroqd.service"]

def sensorServicesCheck():
    print("Service Check")

    for service in servicesList:

        status = subprocess.call(["systemctl", "is-active", "--quiet", service])

        if (status == 0):
            print("Service: " + service + " is running")
        else:
            print("Service: " + service + " is not running!")
    

def main():
    sensorServicesCheck()



if __name__ == '__main__':
    main()