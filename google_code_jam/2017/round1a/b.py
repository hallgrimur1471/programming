#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import sys
from math import floor

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
        print("Case #{}: {}".format(t+1, s))

def solve(N, P, R, Q):
    u = []
    for i in range(N):
        u.append([0]*P)
    for ig in range(P):
        s = []
        r = floor(Q[0][ig]*0.9/R[0])
        while r*R[0] <= Q[0][ig]*1.1:
            if r*R[0] >= Q[0][ig]*0.9:
                s.append(r)
            r += 1

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
