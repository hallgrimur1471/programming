#!/usr/bin/env python3

import sys
import time
from day_10_2_knot_hash import knot_hash

def main():
    start_time = time.time()

    inpt = sys.stdin.read().strip()

    disk = []
    for i in range(0, 128):
        k_hash = knot_hash(inpt+"-"+str(i))
        bits = map(lambda c: bin(int(c, 16))[2:].zfill(4), k_hash)
        bits = ''.join(list(bits))
        disk.append(bits)

    s = sum(map(lambda row: sum(map(int, row)), disk))
    print(s)

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
