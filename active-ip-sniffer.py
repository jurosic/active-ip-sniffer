import os
import signal
from datetime import datetime

try:

    ip_list = list(range(1, 255))

    Active = open(r"Active.txt","w+")
    Unactive = open(r"Unactive.txt", "w+")

    now = datetime.now()
    
    print(now)

    Active.write(str(now))
    Unactive.write(str(now))

    for ip in ip_list:
        
        response = os.popen(f"ping -c 1 192.168.2.{ip}").read()
        #respondIn = (f'.. responded in {response.split("time=")[-1].split(" ")[0]}ms')
        #activeWrite = (f"\nUP 192.168.2.{ip} Ping is successful and IP is connected to router", respondIn)
        
        if "1 received" in response:
            #if "192.168.2.1" in response:
                #print(f"UP 192.168.2.{ip} Ping successful (router)")
                #Active.write(f"\nUP 192.168.2.{ip} Ping is successful and IP is the router")
            #else:
                print(f'\nUP 192.168.2.{ip} Ping is successful and IP is connected to router .. responded in {response.split("time=")[-1].split(" ")[0]}ms')
                Active.write(f'\nUP 192.168.2.{ip} Ping is successful and IP is connected to router .. responded in {response.split("time=")[-1].split(" ")[0]}ms')
        
        else:
            
            Unactive.write(f"\nDOWN 192.168.2.{ip} Ping is unsuccessful and IP is not connected to router .. did not respond")
            print(f"DOWN 192.168.2.{ip} Ping Unsuccessful ..  did not respond")

    Active.write("\n...............END...............\n")
    Active.write(str(datetime.now()))
    Unactive.write("\n...............END...............\n")
    Unactive.write(str(datetime.now()))

except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")
    Active.write("\n...............END...............\n")
    Active.write(str(datetime.now()))
    Unactive.write("\n...............END...............\n")
    Unactive.write(str(datetime.now()))
