#!/bin/bash

# connect from moldel to hive
#ssh ubuntu@hive.local 

# moldel
sudo rsync -avz /home/hallgrimur1471/bashscripts/moldel-mavproxy.sh /usr/local/bin/mavproxy.sh

# rpi
ssh root@lair.local ""
rsync -avz -e "ssh -p 20000 -i ~/.ssh/id_rsa" --progress /home/hallgrimur1471/bashscripts/