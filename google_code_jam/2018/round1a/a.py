#!/usr/bin/env python3

import sys
from sys import stdin, stdout, stderr
from math import floor, ceil

sys.setrecursionlimit(10000)

def main():
    T = int(input())
    for t in range(T):
        R, C, H, V = list(map(int, input().split(' ')))
        w = []
        for i in range(R):
            w.append(input())
        s = solve(R, C, H, V, w)
        print("Case #{}: {}".format(t+1, s))
    pass

def solve(R, C, H, V, w):
    n = 0
    for line in w:
        n += len([x for x in line if x=="@"])
    customers = (H+1)*(V+1)
    if n % customers != 0:
        return "IMPOSSIBLE"
    hd = customers / (H+1)
    hcts = []
    vcts = [0]
    i = 0
    while len(hcts) < H:
        hc = 0
        while hc < hd:
            hc += [x for x in w[i] if x=="@"]
            i += 1
        if hc > hd:
            return "IMPOSSIBLE"
        else:
            hcts.append(i-1)

    vd = hd / (V+1)
    j = 1
    while len(vcts) < V+1:
        cnt = 0
        for k in range(vcts[-1], j):k



def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
