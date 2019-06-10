#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument
import sys
import numpy as np


def main():
    T, W = map(int, input().split(" "))
    for case_num in range(1, T + 1):
        c = 6 * [0]
        for i in range(1, 7):
            prnt(i)
            resp = int(input())
            if resp == -1:
                sys.exit(1)
            c[i - 1] = resp
        a = np.zeros((6, 6), dtype=int)
        for i in range(0, 6):
            a[i][0] = 2 ** ((i + 1) // 1)
            a[i][1] = 2 ** ((i + 1) // 2)
            a[i][2] = 2 ** ((i + 1) // 3)
            a[i][3] = 2 ** ((i + 1) // 4)
            a[i][4] = 2 ** ((i + 1) // 5)
            a[i][5] = 2 ** ((i + 1) // 6)
        c = np.array(c)
        r = np.linalg.solve(a, c)
        r = list(map(int, r))
        r = list(map(str, r))
        prnt(" ".join(r))
        if int(input()) == -1:
            sys.exit(1)


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
