#!/usr/bin/env python3.5
import sys


def main():
    T, N, M = map(int, input().split(" "))
    for case_num in range(1, T + 1):
        m = [17, 16, 13, 11, 9, 7, 5]
        a = 7 * [0]
        for i in range(7):
            prnt(" ".join(18 * [str(m[i])]))
            resp = list(map(int, input().split(" ")))
            if resp == [-1]:
                sys.exit(1)
            a[i] = sum(resp) % m[i]
        i = 0
        G = a[0]
        while i < 7:
            while i < 7 and G % m[i] == a[i]:
                i += 1
            if i < 7:
                i = 0
                G += m[0]
        prnt(G)
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
