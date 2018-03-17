#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import sys

sys.setrecursionlimit(10000)

def main():
    tc = int(input())
    for t in range(tc):
        s = solve()
        print("Case #{}: {}".format(t+1, s))
    pass

def solve():
    pass

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
