import os
import subprocess
import activePortSnifferRunner
import activeIpSnifferRunner



while True:
    subprocess.call('clear', shell=True)
    
    print("╔═╗  ┌─┐  ┌┬┐  ┬  ┬  ┬  ┌─┐       ╦  ╔═╗       ╔═╗  ╔╗╔  ╦  ╔═╗  ╔═╗  ╔═╗  ╦═╗\n╠═╣  │     │   │  └┐┌┘  ├┤   ───  ║  ╠═╝  ───  ╚═╗  ║║║  ║  ╠╣   ╠╣   ║╣   ╠╦╝\n╩ ╩  └─┘   ┴   ┴   └┘   └─┘       ╩  ╩         ╚═╝  ╝╚╝  ╩  ╚    ╚    ╚═╝  ╩╚═")
    
    choice = input("Choose an option:\n 3. Active IP Sniffer\n 4. Active Open Port Sniffer\n q. Quit")

    if choice == "3":
        activeIpSnifferRunner.start()
        subprocess.call('clear', shell=True)
        choice = input("Choose an option:\n 1. Active IP Sniffer\n 2. Active Open Port Sniffer\n")
    
    elif choice == "4":
        activePortSnifferRunner.start()
        subprocess.call('clear', shell=True)
        choice = input("Choose an option:\n 1. Active IP Sniffer\n 2. Active Open Port Sniffer\n")
    
    #elif choice == "3":
        #scanForGateways.start1()
        #choice = input("Choose an option:\n 1. Active IP Sniffer\n 2. Active Open Port Sniffer\n")

    
    else:
        print("That is not a valid option!")
        choice = input()
