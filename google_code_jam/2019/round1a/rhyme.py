#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument
import sys


def solve(n):


def main():
    T = int(input())
    for case_num in range(1, t + 1):
        N = int(input())
        W = []
        for i in range(N):
            W.append(input())
        s = solve(n)
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
