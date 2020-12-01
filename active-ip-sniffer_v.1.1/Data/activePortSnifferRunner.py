import socket
import subprocess
import sys
import os
from datetime import datetime

def start():
    
    try:
        os.mkdir("Log/Ports")
    except:
        pass

    subprocess.call('clear', shell=True)

    remoteServer    = input("Enter a remote host to scan: ") 
    
    fileName = remoteServer.replace('.', '_')
    
    portType = open("Log/Ports/{}.txt".format(fileName), "w+")

    foo = True
    oof = True
    while foo == True:
        portRange1      = input("Select port range from: ")
        try:
            int(portRange1)
            foo = False
        except:
            print(portRange1, " is not a valid int!")
    while oof == True:
        portRange2      = input("Select port range to: ")
        try:
            int(portRange2)
            oof = False
        except:
            print(portRange2, " is not a valid int!")

    remoteServerIP  = socket.gethostbyname(remoteServer)

    print ("-" * 60)
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("-" * 60)

    t1 = datetime.now()


    try:
        for port in range(int(portRange1), int(portRange2)):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print ("Port {}: 	 Open".format(port))
                portType.write("Port {}:     Open\n".format(port))
            sock.close()


    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()

    total =  t2 - t1

    print ('Scanning Completed in: ', total)

    input()
