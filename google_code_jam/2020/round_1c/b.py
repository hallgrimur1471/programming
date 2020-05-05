#!/usr/bin/env python3
import sys
from collections import deque

DEBUG = "ON"


def solve(N, D, A):
    pass


def main():
    sys.setrecursionlimit(10000)
    T = int(input())
    for case_num in range(1, T + 1):
        U = int(input())
        if U != 2:
            sys.exit(1)
        data = []
        for i in range(0, 10 ** 4):
            line = input().split(" ")
            data.append((int(line[0]), line[1]))
        data = list(set(data))
        data.sort()
        p = dict()
        for m, c in data:
            if m >= 10:
                break
            if m not in p:
                p[m] = {c}
            else:
                p[m].add(c)
        for i in reversed(range(2, 10)):
            p[i] = p[i] - p[i - 1]
        known = set()
        for k, v in p.items():
            known.add(list(v)[0])
        zero_found = False
        for i in reversed(range(0, len(data))):
            r = data[i][1]
            for c in r:
                if c not in known:
                    p[0] = {c}
                    zero_found = True
                    break
            if zero_found:
                break
        ans = []
        for i in range(0, 10):
            ans.append(list(p[i])[0])
        ans = "".join(ans)
        prnt("Case #{}: {}".format(case_num, ans))


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
