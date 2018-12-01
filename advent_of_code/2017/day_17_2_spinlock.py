#!/usr/bin/env python3

import sys
import time
from copy import copy, deepcopy

def main():
    start_time = time.time()

    steps = int(sys.stdin.read().strip())
    vortex = [0]
    i = 0

    for val in range(1, 50000000+1):
        vortex_length = val # this is faster
        if val < 10:
            print(vortex)
        if val % 1000000 == 0:
            print(val)
        i = (i + (steps % vortex_length)) % vortex_length
        if i == 0:
            print("inserting after 0: "+str(val))
        #vortex.insert(i+1, val) # inserting to a list is slow!
        i = (i+1) % (vortex_length+1)

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
