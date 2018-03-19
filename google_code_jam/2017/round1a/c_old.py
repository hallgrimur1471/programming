#!/usr/bin/env python3

import sys
from sys import stdin, stdout, stderr
from math import floor, ceil, inf

import numpy
from numpy import zeros

sys.setrecursionlimit(15800)

def main():
    pycharm = False
    if pycharm:
        with open('/home/hallgrimur1471/programming/google_code_jam/2017/round1a/c.ex2') as f:
            tc = int(f.readline())
            for t in range(tc):
                Hd, Ad, Hk, Ak, B, D = list(map(int, f.readline().split(' ')))
                s = solve(Hd, Ad, Hk, Ak, B, D)
                pt("Case #{}: {}".format(t+1, s))
                print("Case #{}: {}".format(t+1, s))
    else:
        tc = int(input())
        for t in range(tc):
            Hd, Ad, Hk, Ak, B, D = list(map(int, input().split(' ')))
            s = solve(Hd, Ad, Hk, Ak, B, D)
            pt("Case #{}: {}".format(t+1, s))
            print("Case #{}: {}".format(t+1, s))

def solve(Hd, Ad, Hk, Ak, B, D):
    def mnt(Md, Hd, Ad, Hk, Ak, B, D):
        if Ad >= Hk:
            print("Returning 1!")
            return 1
        print("Md: {}, Hd: {}, Ad: {}, Hk: {}, Ak: {}, B: {}, D: {}".format(Md, Hd, Ad, Hk, Ak, B, D))
        if Ak == 0:
            T = 2
        else:
            T = ceil(Hd/Ak)
        print("T:", T)
        if T == 1:
            mns = []
            if D > 0 and Hd - (Ak - D) > 0:
                Ak -= D
                Hd -= Ak
                mn = 1 + mnt(Md, Hd, Ad, Hk, Ak, B, D)
                mns.append(mn)
            if Hd < Md and (Ak == 0 or ceil((Md - Ak)/Ak) > 1):
                Hd = Md
                Hd -= Ak
                mn = 1 + mnt(Md, Hd, Ad, Hk, Ak, B, D)
                mns.append(mn)
            if not mns:
                return inf
            return min(mns)
        else:
            mns = []
            if Ad > 0:
                mns.append(1 + mnt(Md, Hd - Ak, Ad, Hk - Ad, Ak, B, D)) # attack
            if B > 0:
                mns.append(1 + mnt(Md, Hd - Ak, Ad + B, Hk, Ak, B, D)) # buff
            if Hd < Md and (Ak == 0 or ceil((Md - Ak)/Ak) > T):
                mns.append(1 + mnt(Md, Md - Ak, Ad, Hk, Ak, B, D)) # cure
            if D > 0 and Ak > 0:
                mns.append(1 + mnt(Md, Hd - Ak, Ad, Hk, Ak - D, B, D)) # debuff
            if not mns:
                return inf
            else:
                return min(mns)
    Md = Hd
    mn = mnt(Md, Hd, Ad, Hk, Ak, B, D)
    if mn == inf:
        return "IMPOSSIBLE"
    return mn

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
