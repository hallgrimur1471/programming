#!/usr/bin/env python3

import sys
from random import randint
from math import floor, ceil


def main():
    T = 100
    prnt(T)
    for case_num in range(1, T + 1):
        R, C = (randint(2, 100), randint(2, 100))
        H, V = (randint(1, R - 1), randint(1, C - 1))
        G = []
        for i in range(R):
            G.append(C * ["."])
        cakes = randint(0, R * C) * ["@"]
        while cakes:
            cake = cakes.pop()
            (i, j) = (randint(0, R - 1), randint(0, C - 1))
            while G[i][j] == cake:
                (i, j) = (randint(0, R - 1), randint(0, C - 1))
            G[i][j] = cake
        prnt(R, C, H, V)
        for i in range(R):
            print("".join(G[i]))


def prnt(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    print(*args, **kwargs)


def dbg(*args, **kwargs):
    return
    if "flush" not in kwargs:
        kwargs["flush"] = True
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    print(*args, **kwargs)


if __name__ == "__main__":
    main()
