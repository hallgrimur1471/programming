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
        with open('/home/hallgrimur1471/programming/google_code_jam/2017/round1a/c.ex3') as f:
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
            pt("Hd: {}  Ad: {}  Hk: {}  Ak: {}  B: {}  D:{}".format(Hd,Ad,Hk,Ak,B,D))
            print("Hd: {}  Ad: {}  Hk: {}  Ak: {}  B: {}  D:{}".format(Hd,Ad,Hk,Ak,B,D))
            s, h = solve(Hd, Ad, Hk, Ak, B, D)
            pt("Case #{}: {}".format(t+1, s))
            #pt("h:", h)
            pt("\n")
            print("Case #{}: {}".format(t+1, s))

def solve(Hd, Ad, Hk, Ak, B, D):
    def mnt(Md, Hd, Ad, Hk, Ak, B, D, has_buffed, has_attacked, h):
        if Hd <= 0:
            return inf, h
        if Ad >= Hk:
            return 1, h+"A"
        mns = []
        if (not has_buffed) and (not has_attacked):
            # debuff, buff, attack or cure?
            if D > 0 and Ak > 0: # debuff?
                ret, h2 = mnt(Md, Hd-(Ak-D), Ad, Hk, Ak-D, B, D, False, False, h+"D")
                mns.append((ret+1, h2))
            if Hd - Ak <= 0 and ceil(Md/Ak) > 2: # cure?
                ret, h2 = mnt(Md, Md-Ak, Ad, Hk, Ak, B, D, False, False, h+"C")
                mns.append((ret+1, h2))
            if B > 0: # buff?
                ret, h2 = mnt(Md, Hd-Ak, Ad+B, Hk, Ak, B, D, True, False, h+"B")
                mns.append((ret+1, h2))
            if True: # attack?
                ret, h2 = mnt(Md, Hd-Ak, Ad, Hk-Ad, Ak, B, D, False, True, h+"A")
                mns.append((ret+1, h2))
        elif has_buffed and (not has_attacked):
            # buff, attack or cure?
            if B > 0: # buff?
                ret, h2 = mnt(Md, Hd-Ak, Ad+B, Hk, Ak, B, D, True, False, h+"B")
                mns.append((ret+1, h2))
            if Hd - Ak <= 0 and ceil(Md/Ak) > 2: # cure?
                ret, h2 = mnt(Md, Md-Ak, Ad, Hk, Ak, B, D, True, False, h+"C")
                mns.append((ret+1, h2))
            if True: # attack?
                ret, h2 = mnt(Md, Hd-Ak, Ad, Hk-Ad, Ak, B, D, True, True, h+"A")
                mns.append((ret+1, h2))
        elif has_attacked:
            # attack or cure?
            if Hd - Ak <= 0 and ceil(Md/Ak) > 2: # cure?
                ret, h2 = mnt(Md, Md-Ak, Ad, Hk, Ak, B, D, True, True, h+"C")
                mns.append((ret+1, h2))
            if True: # attack?
                if Ak == 0:
                    na = ceil(Hk/Ad) # num attacks
                else:
                    na = floor(Hd/Ak)
                na = max(na, 1) # at least 1
                #print("na", na)
                ret, h2 = mnt(Md, Hd-na*Ak, Ad, Hk-na*Ad, Ak, B, D, True, True, h+"A")
                mns.append((ret+na, h2))
        else:
            error("what?")
        if not mns:
            error("wtf?")
        return min(mns)
    Md = Hd
    mn, h = mnt(Md, Hd, Ad, Hk, Ak, B, D, False, False, "")
    if mn == inf:
        return "IMPOSSIBLE", h
    return mn, h

def error(msg):
    print(*args, file=stderr)
    sys.exit(1)

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
