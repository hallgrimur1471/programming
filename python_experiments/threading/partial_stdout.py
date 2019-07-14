#!/usr/bin/env python3

import subprocess
from subprocess import PIPE

from svarmi.utils import error

def execute(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    output = ''

    for line in iter(process.stdout.readline, b""):
        print(line.rstrip().decode("utf-8"))
        output += line.decode("utf-8")

    # did we get an error?
    err = ''.join(map(lambda l: l.decode("utf-8"), process.stderr.readlines()))
    if err:
        error(err)

    process.wait()

execute("./timeconsuming_command.py")
