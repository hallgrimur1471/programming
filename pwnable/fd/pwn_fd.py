#!/usr/bin/env python3.7

import subprocess

magic = int("1234", base=16)
cmd = f"printf 'LETMEWIN\n' | ./fd {magic}"

print("command:")
print(bytes(cmd, encoding="utf-8"))
print()
print("program output:")
subprocess.run(cmd, shell=True)
