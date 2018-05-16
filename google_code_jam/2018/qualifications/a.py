#!/usr/bin/env python3

import sys

def main():
    T = int(input())
    for t in range(1, T+1):
        D, P = input().split(' ')
        D = int(D)
        P = list(P)
        print("Case #{}: {}".format(t, solve(D, P)))

def solve(D, P):
    pwr = 1
    dmg = 0
    for i in range(len(P)):
        if P[i] == 'C':
            pwr *= 2
        elif P[i] == 'S':
            dmg += pwr
        else:
            error("wtf?")

    i = len(P)-1
    cnt = 0
    while dmg > D:
        if i == 0:
            return "IMPOSSIBLE"
        if P[i] == 'C':
            pwr /= 2
            i -= 1
        elif P[i] == 'S' and P[i-1] == 'S':
            i -= 1
        elif P[i] == 'S' and P[i-1] == 'C':
            dmg -= pwr/2
            tmp = P[i]
            P[i] = P[i-1]
            P[i-1] = tmp
            cnt += 1
            if i < len(P)-1:
                i += 1
        else:
            error("nope")
    return cnt

            
            
def error(*msg):
    sys.stderr.write(*msg, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
