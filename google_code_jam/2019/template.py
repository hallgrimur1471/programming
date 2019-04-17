#!/usr/bin/env python3.5
import sys
from collections import deque


def solve(N):
    pass


def main():
    T = int(input())
    for case_num in range(1, T + 1):
        N = int(input())
        s = solve(N)
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