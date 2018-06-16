#!/usr/bin/env python3

import sys
import math

def main():
    lengths = list(map(int, sys.stdin.read().strip().split(',')))
    x = list(range(0,256))
    i = 0
    skip_size = 0

    for d in lengths:
        if i+d >= len(x):
            sublist = x[i:] + x[:d-(len(x)-i)]
        else:
            sublist = x[i:i+d]

        sublist.reverse()

        for j in range(0, len(sublist)):
            x[(i+j) % len(x)] = sublist[j]

        i = (i+d+skip_size) % len(x)
        skip_size += 1

    print(x[0]*x[1])

if __name__ == "__main__":
    main()
