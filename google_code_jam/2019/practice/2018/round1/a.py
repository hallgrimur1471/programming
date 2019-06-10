#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument,unused-variable
# pylint: disable=consider-using-enumerate,too-many-branches
# pylint: disable=inconsistent-return-statements
import sys


def solve(R, C, H, V, G):
    T = 0
    for i in range(R):
        for j in range(C):
            if G[i][j] == "@":
                T += 1
    if (T % (H + 1) != 0) or (T % (V + 1) != 0):
        return "IMPOSSIBLE"
    vcuts = []
    t = 0
    for j in range(C):
        for i in range(R):
            if G[i][j] == "@":
                t += 1
        if t == T // (V + 1):
            t = 0
            if j != C - 1:
                vcuts.append(j)
        elif t > (T // (V + 1)):
            return "IMPOSSIBLE"
    if t != 0:
        return "IMPOSSIBLE"
    rcells = (len(vcuts) + 1) * [0]
    for i in range(R):
        for j in range(C):
            if G[i][j] == "@":
                cj = 0
                while cj < len(vcuts) and j > vcuts[cj]:
                    cj += 1
                rcells[cj] += 1
        if sum(rcells) == T // (H + 1):
            for j in range(len(rcells) - 1):
                if rcells[j] != rcells[j + 1]:
                    return "IMPOSSIBLE"
            for j in range(len((rcells))):
                rcells[j] = 0
        if sum(rcells) > (T // (H + 1)):
            return "IMPOSSIBLE"
    if sum(rcells) != 0:
        return "IMPOSSIBLE"
    return "POSSIBLE"


def main():
    t = int(input())
    for case_num in range(1, t + 1):
        r, c, h, v = map(int, input().split(" "))
        g = []
        for i in range(r):
            g.append(input())
        s = solve(r, c, h, v, g)
        prnt("Case #{}: {}".format(case_num, s))


def prnt(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    print(*args, **kwargs)


def dbg(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    print(*args, **kwargs)


if __name__ == "__main__":
    main()
