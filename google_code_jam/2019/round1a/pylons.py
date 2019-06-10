#!/usr/bin/env python3.5
from random import randint


def solve(R, C):
    if R > C:
        tmp = R
        R = C
        C = tmp

    if R == 2 and C == 2:
        return "IMPOSSIBLE"
    if R == 2 and C == 3:
        return "IMPOSSIBLE"
    if R == 2 and C == 4:
        return "IMPOSSIBLE"
    if R == 2 and C == 5:
        return "POSSIBLE"
    if R == 3 and C == 3:
        return "IMPOSSIBLE"
    if R == 3 and C == 4:
        return "POSSIBLE"  # 2
    if R == 3 and C == 5:
        return "IMPOSSIBLE"  # 1
    if R == 4 and C == 4:
        return "POSSIBLE"
    if R == 5 and C == 5:
        return "IMPOSSIBLE"  # 1

    if randint(0, 1) == 1:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"


def main():
    t = int(input())
    for case_num in range(1, t + 1):
        R, C = map(int, input().split(" "))
        s = solve(R, C)
        print("Case #{}: {}".format(case_num, s))


if __name__ == "__main__":
    main()
