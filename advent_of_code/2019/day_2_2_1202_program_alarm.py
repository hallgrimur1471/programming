#!/usr/bin/env python3.7

from copy import copy


def main():
    original_p = list(map(int, input().split(",")))
    for noun in range(0, 100):
        for verb in range(0, 100):
            p = copy(original_p)
            p[1] = noun
            p[2] = verb
            if solve(p) == 19690720:
                calculated_anwser = 100 * noun + verb
                print(f"noun: {noun}, verb: {verb}")
                print(f"100 * noun + verb: {calculated_anwser}")


def solve(p):
    i = 0
    while p[i] != 99:
        p = process(p, i)
        i += 4
    return p[0]


def process(p, i):
    if p[i] == 1:
        p[p[i + 3]] = p[p[i + 1]] + p[p[i + 2]]
    elif p[i] == 2:
        p[p[i + 3]] = p[p[i + 1]] * p[p[i + 2]]
    else:
        raise RuntimeError()

    return p


if __name__ == "__main__":
    main()
