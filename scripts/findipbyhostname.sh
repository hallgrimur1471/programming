#!/bin/bash
if [ $# -eq 1 ] && [ $1 = "-h" -o $1 = "--help" ] || [ $# -eq 0 ]
then
	printf "Usage: findipbyhostname HOSTNAME\n"
	printf "  Finds local ip address of device with a hostname in the LAN.\n"
	printf "  Outputs nothing if no device found and returns with a non-zero exit code.\n"
	exit 0
fi

if [ $# -gt 1 ]
then
	echo "Error: too many input arguments." >> /dev/stderr
	exit 1
fi

ip_address=$(getent hosts ${1}.local | awk '{print $1}')
if [ ! -z "$ip_address" ]
then
    echo "$ip_address"
    exit 0
else
    exit 1
fi
