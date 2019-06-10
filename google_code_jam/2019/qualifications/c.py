#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument
import sys
from math import gcd


def solve(n, L, c):
    s = (L + 1) * [0]
    i = 0
    while c[i] == c[i + 1]:
        i += 1
    cd = gcd(c[i], c[i + 1])
    s[i + 1] = cd
    for j in reversed(range(0, i + 1)):
        s[j] = c[j] // s[j + 1]
    for j in range(i + 2, L + 1):
        s[j] = c[j - 1] // s[j - 1]
    pr = sorted(list(set(s)))
    s = list(map(lambda x: chr(pr.index(x) + ord("A")), s))
    s = "".join(s)
    return s


def main():
    t = int(input())
    for case_num in range(1, t + 1):
        n, L = list(map(int, input().split(" ")))
        c = list(map(int, input().split(" ")))
        s = solve(n, L, c)
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
