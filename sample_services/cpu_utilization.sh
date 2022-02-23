#!/bin/bash

DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo "CPU utilization service started at ${DATE}" | systemd-cat -p info

sar -u 5