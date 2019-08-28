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

### install python 3.5 & pip
##apt-get install -y python3-dev python3-pip python3-tk
#
## python 3.6 is installed by default
#
## install python 3.7 & pip
#add-apt-repository -y ppa:deadsnakes/ppa
#apt-get update
#apt-get install -y python3.7
#apt-get install -y python3.7-dev
#apt-get install -y python3.7-tk
#
## install pip for all python versions.
## The order of lines is important here to pass the install test
#apt-get install -y curl
#curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
#python3.7 /tmp/get-pip.py
#python3.6 /tmp/get-pip.py
#python2.7 /tmp/get-pip.py
#rm /tmp/get-pip.py
