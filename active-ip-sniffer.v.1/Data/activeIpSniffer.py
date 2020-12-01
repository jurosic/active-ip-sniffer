import os
import activeIpSnifferRunner

print("╔═╗  ┌─┐  ┌┬┐  ┬  ┬  ┬  ┌─┐       ╦  ╔═╗       ╔═╗  ╔╗╔  ╦  ╔═╗  ╔═╗  ╔═╗  ╦═╗\n╠═╣  │     │   │  └┐┌┘  ├┤   ───  ║  ╠═╝  ───  ╚═╗  ║║║  ║  ╠╣   ╠╣   ║╣   ╠╦╝\n╩ ╩  └─┘   ┴   ┴   └┘   └─┘       ╩  ╩         ╚═╝  ╝╚╝  ╩  ╚    ╚    ╚═╝  ╩╚═")

choice = input("Choose an option:\n 1. Active IP Sniffer\n Nothing else is here yet!\n")

while True:

    if choice == "1":
        activeIpSnifferRunner.start()
        choice = input("Choose an option:\n 1. Active IP Sniffer\n Nothing else is here yet!\n")
    
    else:
        print("That is not a valid option!")
        choice = input()
