#!/usr/bin/env python3.7

import subprocess

for i in range(0, 1):
    cmd = ["./print_input_info", "\xfff6"]
    out = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(i, out.stdout.decode().rstrip())
