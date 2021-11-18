#!/bin/bash

DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo "Example service started at ${DATE}" | systemd-cat -p info

while :
do
echo "Looping...";
sleep 30;
done