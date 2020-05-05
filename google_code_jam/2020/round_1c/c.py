#!/usr/bin/env python3
import sys
from collections import deque

DEBUG = "ON"


def solve(N, D, A):
    A.sort()
    if D == 2:
        if len(A) == len(set(A)):
            return 1
        return 0
    elif D == 3:
        for i in range(2, len(A)):
            if A[i] == A[i - 1] and A[i - 1] == A[i - 2]:
                return 0
        doubled_exists = False
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                if A[i] * 2 == A[j]:
                    doubled_exists = True
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                if i != len(A) - 1:
                    return 1
                else:
                    if doubled_exists:
                        return 1
                    else:
                        return 2
        if doubled_exists:
            return 1
        return 2
    else:
        sys.exit(1)


def main():
    sys.setrecursionlimit(10000)
    T = int(input())
    for case_num in range(1, T + 1):
        N, D = map(int, input().split(" "))
        A = list(map(int, input().split(" ")))
        s = solve(N, D, A)
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
