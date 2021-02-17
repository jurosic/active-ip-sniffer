while [ 1 = 1 ]
do
    clear 
    
    echo "!!!MAIN MENU!!!"
    
read -p "Choose an option:
1. Active IP Sniffer
2. Scan For Gateways
q. Quit 
" option
    
    if [ "$option" = 1 ]
    then 
        python3.9 Data/activeIpSniffer.py
        read nothing
    
    elif [ "$option" = 2 ]
    then
        sudo iwlist wlp2s0 scanning | egrep 'Cell |Encryption|Quality|Last beacon|ESSID' 2>&1 | tee Log/Gateways.txt
        read nothing

    elif [ "$option" = q ]
    then
        echo "Quitting!"
        exit
    else
        echo "That is not a valid option!"
        read nothing
    fi
done
