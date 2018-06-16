#!/usr/bin/env python3

import sys
from sys import stdin, stdout, stderr
from math import floor, ceil

sys.setrecursionlimit(10000)

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        W = list(map(int, input().split(' ')))
        s = solve(N, W)
        print("Case #{}: {}".format(t+1, s))

def solve(N, W):
    c = 0
    for i in range(len(W)-1):
        if W[i] < 6*W[i+1]:
            c += 1
    return c

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
