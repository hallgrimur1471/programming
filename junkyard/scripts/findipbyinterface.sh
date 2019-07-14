#!/bin/bash
if [ $# -eq 1 ] && [ $1 = "-h" -o $1 = "--help" ]
then
	printf "Usage:\n"
	printf "  findipbyinterface [interface1 [interface2 ... ]]\n"
	printf "    TODO: write this help"
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

if [ ! -z $SEARCHSTRING ]
then
	echo "$SEARCHSTRING"
	exit 0
else
	exit 1
fi
