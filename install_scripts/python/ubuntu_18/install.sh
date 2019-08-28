#!/usr/bin/env bash

# this script install python2.7, python3.6, python3.7, pip and pip3

# stop on errors
set -e

# display commands
set -x

# install python2.7
apt-get install -y python

# install python3.6
apt-get install -y python3

# install python3.7
apt-get install -y python3.7

# install pip for python2.7
apt-get install -y python-pip

# install pip for python3.6 and 3.7
apt-get install -y python3-pip
