#!/usr/bin/env python3.7

import subprocess

colliding_password = (
    "54 15 21 115 -67 -31 -67 -62 -44 -2 120 "
    + "-15 -102 -10 -1 -110 -117 35 -111 103"
)  # found using find_collission.c

cmd = f"./col `../utils/print_bytes {colliding_password}`"
print(cmd)
subprocess.run(cmd, shell=True)
