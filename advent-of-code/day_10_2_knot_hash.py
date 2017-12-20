#!/usr/bin/env python3

import sys
import math
import itertools
from copy import copy

def main():
    inpt = sys.stdin.read().strip()
    print(knot_hash(inpt))

def knot_hash(inpt):
    lengths = list(map(ord, inpt))
    suffix = [17, 31, 73, 47, 23]
    lengths += suffix
    x = list(range(0,256))
    i = 0
    skip_size = 0

    for _ in itertools.repeat(None, 64):
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

    sparse_hash = copy(x)

    dense_hash = []
    for i in range(0,16):
        k = sparse_hash[16*i]
        for j in range(1,16):
            k = k ^ sparse_hash[16*i + j]
        dense_hash.append(k)

    dense_hash = ''.join(list(map(lambda num: "{0:0{1}x}".format(num, 2), dense_hash)))
    return dense_hash

if __name__ == "__main__":
    main()
