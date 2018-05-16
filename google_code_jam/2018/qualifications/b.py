#!/usr/bin/env python3

import sys
from sys import stdin, stdout, stderr
from math import floor, ceil

#sys.setrecursionlimit(10000)

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        V = input().split(' ')
        V = list(map(int, V))
        s = solve(N, V)
        pt("Case #{}: {}".format(t+1, s))
    pass

def solve(N, V):
    a = []
    b = []
    for i in range(N):
        if i % 2 == 0:
            a.append(V[i])
        else:
            b.append(V[i])

    a.sort()
    b.sort()

    d = []
    for i in range(len(a)):
        d.append(a[i])
        if i < len(b):
            d.append(b[i])

    for i in range(N-1):
        if d[i] > d[i+1]:
            return i
    return "OK"

def pt(*args):
    print(*args, file=stdout)

if __name__ == "__main__":
    main()
