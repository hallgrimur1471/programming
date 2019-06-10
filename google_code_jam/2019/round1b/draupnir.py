#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument
import sys


def main():
    T, W = map(int, input().split(" "))
    for case_num in range(1, T + 1):



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
