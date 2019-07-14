#!/bin/bash
if [ $# -eq 1 ] && [ $1 = "-h" -o $1 = "--help" ]
then
	printf "Usage:\n"
	printf "  findmysubnet [interface1 [interface2 ... ]]\n"
	printf "    Prints the first three numbers of the subnet the computer is connected to."
	printf    " For example if the computer's wireless interface has the address 192.168.1.133 on the subnet, findmysubnet will print 192.168.1\n"
	printf "    If interfaces (see ifconfig) are specified findmysubnet will only print subnets those interfaces are connected to.\n"
	printf "    Duplicate subnets are only printed once. If no interfaces are specified findmysubnet will use all active interfaces except the local loopback interface.\n"
	exit 0
fi

# get appropriate contents of ifconfig
if [ $# -eq 0 ]
then
	SEARCHSTRING=$( ifconfig )
else
	SEARCHSTRING=""
	for interface in $@
	do
		SEARCHSTRING+=$( ifconfig ${interface} )
		SEARCHSTRING+=$'\n'
	done
fi

# isolate the ip addresses
SEARCHSTRING=$(echo "$SEARCHSTRING" | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*')

# exclude the local loopback address
SEARCHSTRING=$(echo "$SEARCHSTRING" | grep -v '127.0.0.1')

# only display subnet (not last the last number of the address)
SEARCHSTRING=$(echo "$SEARCHSTRING" | grep -Eo '([0-9]*\.){2}[0-9]')

echo "$SEARCHSTRING"