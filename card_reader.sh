#!/bin/bash
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
    echo "----------------------------"
done
