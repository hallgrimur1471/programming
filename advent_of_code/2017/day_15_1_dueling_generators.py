#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    matches = 0

    a = int(sys.stdin.readline().strip().split(' ')[-1])
    b = int(sys.stdin.readline().strip().split(' ')[-1])

    a_factor = 16807
    b_factor = 48271

    magic = 2147483647

    for i in range(0,40000000):
        a = gen(a, a_factor, magic)
        a_bits = bin(a)[2:].zfill(32)[-16:]
        b = gen(b, b_factor, magic)
        b_bits = bin(b)[2:].zfill(32)[-16:]
    
        if a_bits == b_bits:
            matches += 1

    print(matches)

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def gen(v, f, n):
    return (v*f) % n

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
