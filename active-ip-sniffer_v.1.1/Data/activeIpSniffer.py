import os
import subprocess
import activePortSnifferRunner
import activeIpSnifferRunner

print("╔═╗  ┌─┐  ┌┬┐  ┬  ┬  ┬  ┌─┐       ╦  ╔═╗       ╔═╗  ╔╗╔  ╦  ╔═╗  ╔═╗  ╔═╗  ╦═╗\n╠═╣  │     │   │  └┐┌┘  ├┤   ───  ║  ╠═╝  ───  ╚═╗  ║║║  ║  ╠╣   ╠╣   ║╣   ╠╦╝\n╩ ╩  └─┘   ┴   ┴   └┘   └─┘       ╩  ╩         ╚═╝  ╝╚╝  ╩  ╚    ╚    ╚═╝  ╩╚═")

choice = input("Choose an option:\n 1. Active IP Sniffer\n 2. Active Open Port Sniffer\n")

while True:

    if choice == "1":
        activeIpSnifferRunner.start()
        subprocess.call('clear', shell=True)
        choice = input("Choose an option:\n 1. Active IP Sniffer\n 2. Active Open Port Sniffer\n")
    
    elif choice == "2":
        activePortSnifferRunner.start()
        subprocess.call('clear', shell=True)
        choice = input("Choose an option:\n 1. Active IP Sniffer\n 2. Active Open Port Sniffer\n")
    
    else:
        print("That is not a valid option!")
        choice = input()
