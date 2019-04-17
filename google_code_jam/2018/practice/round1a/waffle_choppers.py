#!/usr/bin/env python3
import sys

DEBUG = "OFF"


def solve(R, C, H, V, G):
    dbg("R:", R, "C:", C, "H:", H, "V:", V, "G:")
    for line in G:
        dbg(line)
    T = 0
    for i in range(R):
        for j in range(C):
            if G[i][j] == "@":
                T += 1
    dbg("T:", T, "H:", H, "V:", V)
    if (T % (H + 1) != 0) or (T % (V + 1) != 0):
        dbg(4)
        return "IMPOSSIBLE"
    vcuts = []
    t = 0
    for j in range(C):
        for i in range(R):
            if G[i][j] == "@":
                t += 1
        if t == T // (V + 1):
            t = 0
            if j != C - 1 and len(vcuts) < V:
                vcuts.append(j)
        elif t > (T // (V + 1)):
            dbg(4)
            return "IMPOSSIBLE"
    dbg("vcuts:", vcuts)
    if t != 0:
        dbg(5)
        return "IMPOSSIBLE"
    rcells = (len(vcuts) + 1) * [0]
    for i in range(R):
        for j in range(C):
            if G[i][j] == "@":
                cj = 0
                while cj < len(vcuts) and j > vcuts[cj]:
                    cj += 1
                rcells[cj] += 1
        dbg("rcells:", rcells)
        if sum(rcells) == T // (H + 1):
            for j in range(len(rcells) - 1):
                if rcells[j] != rcells[j + 1]:
                    dbg(6)
                    return "IMPOSSIBLE"
                if rcells[0] != T // ((H + 1) * (V + 1)):
                    dbg("7")
                    return "IMPOSSIBLE"
            for j in range(len((rcells))):
                rcells[j] = 0
        elif sum(rcells) > (T // (H + 1)):
            dbg("8")
            return "IMPOSSIBLE"
    if sum(rcells) != 0:
        dbg("last")
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
    if DEBUG != "ON":
        return
    if "flush" not in kwargs:
        kwargs["flush"] = True
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    print(*args, **kwargs)


if __name__ == "__main__":
    main()
