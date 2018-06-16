#!/usr/bin/env python3

import sys
#from sys import stdin, stdout, stderr
from math import floor, ceil

#sys.setrecursionlimit(10000)

def main():
    T = int(input())
    for t in range(T):
        N, L = list(map(int, input().split(' ')))
        s = solve(N, L)
        print("Case #{}: {}".format(t+1, s))

def solve(N, L):
    w = []
    for i in range(N):
        w.append(input())
    for i in range(len(w)):
        w[i] = ''.join(sorted(w[i]))
    w = list(set(w))
    d = [0]*len(w)
    for i, x in enumerate(w):
        last = x[0]
        OK = False
        for j in range(len(x)):
            if x[j] != last:
                OK = True
            last = x[j]
        if not OK:
            d[i] = 1
    w = [x[0] for x in zip(w,d) if x[1]==0]
    if not w:
        return '-'
    else:
        return ''.join(list(reversed(w[0])))

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
