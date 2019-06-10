#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument,unused-variable,too-many-locals
# pylint: disable=too-many-statements,too-many-branches
import sys
from collections import deque


def contains_unknowns(v):
    for x in v:
        (length, unknowns) = x
        if unknowns != 0 and length != unknowns:
            return True
    return False


def process(n, b, f):
    v = deque()
    v.append((n, b))
    while contains_unknowns(v):
        v2 = deque()
        for (length, unkowns) in v:
            left_length = length // 2
            right_length = length - (length // 2)
            v2.append((left_length, right_length))
        s = []
        for (zeros, ones) in v2:
            s += zeros * ["0"]
            s += ones * ["1"]
        prnt("".join(s))
        a = input().rstrip()
        if a == "-1":
            sys.exit(1)
        a2 = deque()
        i = 0
        for (length, unknowns) in v:
            num_zeros = 0
            j = i
            while i - j < (length // 2) and i < len(a) and a[i] == "0":
                num_zeros += 1
                i += 1
            missing_zeros = unknowns - num_zeros
            missing_ones = unknowns - missing_zeros
            a2.append((missing_zeros, missing_ones))
            while (
                i - j < (length - (length // 2)) and i < len(a) and a[i] == "1"
            ):
                i += 1
        assert len(v) == len(a2)
        for _ in range(len(v)):
            (left_length, right_length) = v2.popleft()
            (missing_zeros, missing_ones) = a2.popleft()
            assert v[0][1] == (missing_zeros + missing_ones)
            if v[0][1] == 0 or v[0][0] == v[0][1]:
                v.rotate(-1)
            else:
                v.popleft()
                v.append((left_length, missing_zeros))
                v.append((right_length, missing_ones))
    sol = []
    i = 0
    while v:
        (length, broken) = v.popleft()
        if not broken:
            i += length
            continue
        while broken:
            sol.append(i)
            broken -= 1
            i += 1
    prnt(" ".join(map(str, sol)))
    a = input().rstrip()
    if a == "-1":
        sys.exit(1)


def main():
    t = int(input())
    for case_num in range(1, t + 1):
        n, b, f = list(map(int, input().split(" ")))
        process(n, b, f)


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
