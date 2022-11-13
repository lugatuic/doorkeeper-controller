#!/bin/bash

function call_open_door {
    #add if statment to check if returned data is valide then open door
    if [ $1 = "1" ]
    then
        echo "Access Granted!"
        python $(dirname $0)/open_door.py
    fi
}

allowable=()

clear
while [ 1 ]
do
    echo "Please Swipe Your Card (Press Enter to Exit):"
    read data
 
    if [ "$data" = "" ]
    then
        echo "Exiting"
        exit 0
    fi
    echo
    num="$(echo "$data"|cut -d\B -f2|cut -d\^ -f1)"
    uin="${num:4:9}"
    cardholder="$(echo "$data"|cut -d\^ -f2|cut -d\/ -f1)"
    university="$(echo "$data"|cut -d\/ -f2|cut -d\^ -f1)"
    expDate="$(echo "$data"|cut -d\^ -f3)"
    expDate="${expDate:0:2}/${expDate:2:2}"

    echo "Card Number: $num"
    echo "UIN: $uin"
    echo "Card Holder: $university $cardholder"
    echo "Card Expires(yr/mo): $expDate"
    echo "Swipe Timestamp: `date`"
    echo "----------------------------"

    if [ $university = "UNIVERSITY" ] && [ $cardholder = "CARDHOLDER" ];
    then
        if [[ " ${allowable[@]} " =~ " ${uin} " ]]; then
          call_open_door "1"
        fi
        #result="$(curl -d "UIN=$uin" "localhost")"
        #get return data and pass off to function
        #call_open_door $result
    fi

done
