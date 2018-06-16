#!/usr/bin/env python3

import sys
import operator
from math import floor, ceil

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        if N == -1:
            sys.exit(1)
        q = [0]*N
        s = [0]*N
        for i in range(N):
            judge = input()
            if judge == "-1":
                sys.exit(1)
            L = list(map(int, judge.split(' ')))
            L = L[1:]
            C = [0]*N
            for j in L:
                C[j] = 1
                q[j] += 1
            possibilities = [(x[0],x[3]) for x in zip(q,s,C,list(range(0,N))) if x[1]!=1 and x[2]==1]
            if not possibilities:
                pt(-1)
            else:
                possibilities.sort(key=lambda x: x[0])
                mi = possibilities[0][1]
                #mv = min(possibilities)
                #mi = q.index(mv)
                s[mi] = 1
                pt(mi)

def pt(*args):
    print(*args, end='\n', file=sys.stdout, flush=True)

if __name__ == "__main__":
    main()
