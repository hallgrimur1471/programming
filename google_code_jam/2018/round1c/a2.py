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
    if L == 1:
        return '-'
    if (len(list(set(''.join(w)))))**L == N:
        return '-'
    p = [0]*L
    k = 0
    new = w[0]
    while ''.join(new) in w:
        new = []
        for i, v in enumerate(p):
            new.append(w[v][i])
        while p[k] == N-1:
            p[k] = 0
            k += 1
            if k==L:
                return '-'
        p[k] += 1
        k = 0
    return ''.join(new)


def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
