#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    # construct firewall
    firewall = dict()
    for line in sys.stdin:
        line = list(map(int, line.strip().split(": ")))
        field = line[0]
        laser_range = line[1]
        firewall[field] = laser_range

    # find delay to escape through
    delay = -1
    passes_all = False
    while not passes_all:
        delay += 1

        passes_all = True
        for field, laser_range in firewall.items():
            if does_not_pass(field, laser_range, delay):
                passes_all = False
                break

    print("did not get caught using delay: "+str(delay))
    print("runtime: "+seconds_to_hms(time.time()-start_time))

def does_not_pass(f, r, d):
    a = d+f # packets arrives to layer at this time
    return a % (2*r-2) == 0

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
