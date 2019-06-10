#!/usr/bin/env python3

def solve(D, N):
    for i in range(0, N):
        for j in range(0, 6):
            r = D[i][j]
            v = [i]
            for x in range(0, N):
                for y in range(0, 6):
                    s = D[x][y]
                    if s == r+1:
                        pass
    return len(D)

T = int(input())
for t in range(0, T):
    N = int(input())
    D = []
    for i in range(0, N):
        D.append(list(map(int, input().split(' '))))
    r = solve(D, N)
    print("Case #1: {}".format(r))
