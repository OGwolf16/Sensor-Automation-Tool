#Sensor Service Check Version 1.0
#Owen Garland
#TODO
#Check through the logs for any errors.

import os 
import subprocess

#list of services to check.
servicesList = ["rtk_bypassd.service", "suricata6.service", "rtk_zeroqd.service"]

#allows for us to check services automatically to determine if they are running in a good state or not.
def sensorServicesCheck():
    print("Service Check")

    for service in servicesList:

        status = subprocess.call(["systemctl", "is-active", "--quiet", service]) # Calls systemctl on the system with the service to determine if it is running or not.

        if (status == 0):
            print("Service: " + service + " is running") #Service is running
        else:
            print("Service: " + service + " is not running!") # Service is not running or not found.

#The config checks goal is to automatically determine if they have inconsientcess between the two configs because if there is a local configured and a generated config 
#from volitle configs. The Local config will be taken over so if they try to make any changes to the configureation of the sensor their changes will be overruled by the local.
def configsCheck():
    print("Configs Check")
    if(os.path.isfile('TestFiles/testGeneratedFile.yaml') and os.path.isfile('TestFiles/testLocalFile.yaml')): # If both files are present please compare and see the diffs
        generatedConfig = open('TestFiles/testGeneratedFile.yaml')
        localConfig = open('TestFiles/testLocalFile.yaml')

        generatedConfig_line = generatedConfig.readline() 
        localConfig_line = localConfig.readline() 

        line_no = 1
 
        print("Different Lines in Both Files") 
        while generatedConfig_line != '' or localConfig_line != '': 
        
            # Removing whitespaces 
            generatedConfig_line = generatedConfig_line.rstrip() 
            localConfig_line = localConfig_line.rstrip() 
        
            # Compare the lines from both file 
            if generatedConfig_line != localConfig_line: 
                
                # otherwise output the line on file1 and use @ sign 
                if generatedConfig_line == '': 
                    print("@", "Line-%d" % line_no, generatedConfig_line) 
                else: 
                    print("@-", "Line-%d" % line_no, generatedConfig_line) 
                    
                # otherwise output the line on file2 and use # sign 
                if localConfig_line == '': 
                    print("#", "Line-%d" % line_no, localConfig_line) 
                else: 
                    print("#+", "Line-%d" % line_no, localConfig_line) 
        
                # Print a empty line 
                print() 
        
            # Read the next line from the file 
            generatedConfig_line = generatedConfig.readline() 
            localConfig_line = localConfig.readline() 
        
            line_no += 1
        #Close the files
        generatedConfig.close() 
        localConfig.close() 
    elif (os.path.isfile('TestFiles/testGeneratedFile.yaml')):
        print("Please check and ensure that the configuration in this file is correct.\n ")
        print("TestFiles/testGeneratedFile.yaml")
    elif (os.path.isfile('TestFiles/testLocalFile.yaml')):
        print("Please check and ensure that the configuration in this file is correct.\n ")
        print("TestFiles/testLocalFile.yaml")
    else:
        print("Files not found!")



def main():
    print("="*50)
    sensorServicesCheck()
    print("="*50)
    configsCheck()
    print("="*50)



if __name__ == '__main__':
    main()