#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import sys
from math import floor, ceil

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
    m = []
    for i in range(N):
        m.append([[0]]*P)
    for i in range(N):
        for j in range(P):
            mn = ceil((10/11)*Q[i][j]/R[i])
            mx = floor((10/9)*Q[i][j]/R[i])
            m[i][j] = list(range(mn, mx+1))
    if N == 1:
        return len([x for x in m[0] if x])
    else: # N == 2
        def maximum_matching(c, rv):
            if c == P:
                return len(rv)
            s = m[0][c]
            cands = m2[c]
            if not cands:
                return maximum_matching(c+1, rv)
            mxs = []
            for cand in cands:
                mx = maximum_matching(c+1, rv + [cand])
                mxs.append(mx)
            return max(mxs)
        m2 = {}
        for c in range(P):
            m2[c] = []
            s = m[0][c]
            #if any([sp in r for sp in s]):
            #    m2[c].append(i)
            brk = False
            for i, r in enumerate(m[1]):
                for sp in s:
                    if sp in r:
                        m2[c].append(i)
                        brk = True
                        break
                if brk == True:
                    break
        return maximum_matching(0, [])

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
