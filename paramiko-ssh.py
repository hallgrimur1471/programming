#!/usr/bin/env python

import paramiko

ssh = paramiko.SSHClient()

address = "192.168.1.86"
port = 22
username = "pi"

ssh.connect(address, port, username, timeout=10, key_filename="/home/hallgrimur1471/.ssh/id_rsa")
