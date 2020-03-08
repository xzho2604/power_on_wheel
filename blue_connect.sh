#! /bin/bash

# auto connect the bluetooth controller
while :
do
    statu=`sudo l2ping -c 1 A0:AB:51:05:B8:A4`
    echo "the status:" ,$status
    if [ -z $status ] # connected
    then
        echo "ps controller not connect retrying..."
        echo "connect A0:AB:51:05:B8:A4" | bluetoothctl
    else # connected
        echo "ps controller connected done!"
        break
    fi
done


