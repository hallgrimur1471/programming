#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import sys

sys.setrecursionlimit(10000)

def main():
    tc = int(input())
    for t in range(tc):
        r, c = map(int, input().split())
        cake = []
        for i in range(r):
            cake.append(list(input()))
        print("Case #{}:".format(t+1))
        solve(r, c, cake)

def solve(r, c, cake):
    for i in range(0, r):
        current = None
        for j in range(c):
            if cake[i][j] != '?':
                current = cake[i][j]
            elif cake[i][j] == '?' and current is not None:
                cake[i][j] = current
            elif cake[i][j] == '?' and current is None:
                pass
    for i in range(0, r):
        current = None
        for j in range(c-1, 0-1, -1):
            if cake[i][j] != '?':
                current = cake[i][j]
            elif cake[i][j] == '?' and current is not None:
                cake[i][j] = current
            elif cake[i][j] == '?' and current is None:
                pass
    for j in range(0, c):
        current = None
        for i in range(0, r):
            if cake[i][j] != '?':
                current = cake[i][j]
            elif cake[i][j] == '?' and current is not None:
                cake[i][j] = current
            elif cake[i][j] == '?' and current is None:
                pass
    for j in range(0, c):
        current = None
        for i in range(r-1, 0-1, -1):
            if cake[i][j] != '?':
                current = cake[i][j]
            elif cake[i][j] == '?' and current is not None:
                cake[i][j] = current
            elif cake[i][j] == '?' and current is None:
                pass
    for row in cake:
        print(''.join(row))

def pt(*args):
    print(*args, file=stderr)

if __name__ == "__main__":
    main()
