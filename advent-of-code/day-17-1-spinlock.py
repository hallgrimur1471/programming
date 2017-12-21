#!/usr/bin/env python3

import sys
import time
from copy import copy, deepcopy

def main():
    start_time = time.time()

    steps = int(sys.stdin.read().strip())
    vortex = [0]
    i = 0

    for val in range(1, 2018):
        i = (i + (steps % len(vortex))) % len(vortex)
        vortex.insert(i+1, val)
        i = (i+1) % len(vortex)

    print(vortex[(vortex.index(2017)+1) % len(vortex)])

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
