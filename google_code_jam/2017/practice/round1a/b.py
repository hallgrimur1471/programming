#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import sys
from math import floor, ceil

import numpy as np
from numpy import zeros

sys.setrecursionlimit(10000)

def main():
    tc = int(input())
    for t in range(tc):
        N,P = map(int, input().split(' '))
        R = list(map(int, input().split(' ')))
        Q = []
        for i in range(N):
            Q.append(list(map(int, input().split(' '))))
        s = solve(N, P, R, Q)
        pt("Case #{}: {}".format(t+1, s))
        print("Case #{}: {}".format(t+1, s))

def solve(N, P, R, Q):
    m = zeros(shape=(N,P), dtype=int).tolist()
    for i in range(N):
        for j in range(P):
            mn = ceil((10/11)*Q[i][j]/R[i])
            mx = floor((10/9)*Q[i][j]/R[i])
            m[i][j] = (mn, mx)
    rv = zeros(shape=(N,P), dtype=int).tolist()
    m = list(map(sorted, m))
    c = 0
    def rd(i, j):
        nonlocal c, rv
        u = m[i][j]
        if u[0] > u[1]:
            return
        if i == N-1:
            c += 1
            return
        r = 0
        while True:
            if rv[i+1][r] == 0:
                v = m[i+1][r]
                if u[1] >= v[0] and u[0] <= v[1]:
                    break
            r += 1
            if r >= P:
                return
        rv[i+1][r] = 1
        rd(i+1, r)
    for j in range(P):
        rd(0, j)
    return c

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
