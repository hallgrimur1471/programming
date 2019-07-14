#!/usr/bin/env python3

import sys
from time import sleep

for i in range(5):
    print(i, flush=True)
    if i==3:
        sys.stderr.write("whoopsie!")
        sys.exit(1)
    sleep(1)
