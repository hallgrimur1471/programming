#!/usr/bin/env python3
import sys
from collections import deque

DEBUG = "ON"


def solve(R, B, C, m, s, p):
    def f(t):
        cap = []
        for i in range(C):
            cap.append(max(0, min(m[i], (t - p[i]) // s[i])))
        cap.sort(reverse=True)
        if sum(cap[0:R]) >= B:
            return 1
        return 0

    max_T = B * max(s) + max(p)
    i = 0
    j = max_T + 1
    while i != j:
        mid = i + ((j - i) // 2)
        if f(mid) < 1:
            i = mid + 1
        else:
            j = mid
    return i


def main():
    sys.setrecursionlimit(10000)
    T = int(input())
    for case_num in range(1, T + 1):
        R, B, C = map(int, input().split(" "))
        m, s, p = [C * [0] for _ in range(3)]
        for i in range(C):
            m[i], s[i], p[i] = map(int, input().split(" "))
        s = solve(R, B, C, m, s, p)
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
