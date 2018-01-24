#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import sys

sys.setrecursionlimit(10000)

def main():
    tc = int(input())
    for t in range(1, tc+1):
        a = input().split(' ')
        S = a[0]
        K = int(a[1])
        pt("K", K)
        r = solve(S, K, 0)
        pt("Case #{}: {}".format(t, r))
        print("Case #{}: {}".format(t, r))

def solve(S, K, y):
    S = list(S)
    pt("S", ''.join(S))
    if all([s=='+' for s in S]):
        return y
    i = 0
    while S[i] == '+' and i < len(S):
        i += 1
    if i+K-1 >= len(S):
        return "IMPOSSIBLE"
    S = flip(S, i, K)
    return solve(S, K, y+1)

def flip(S, i, K):
    for x in range(i, i+K):
        if S[x]=='+':
            S[x] = '-'
        else:
            S[x] = '+'
    return S

def pt(*args):
    return
    print(*args, file=stderr)

main()
