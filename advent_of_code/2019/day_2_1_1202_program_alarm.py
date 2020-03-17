#!/usr/bin/env python3.7


def main():
    p = list(map(int, input().split(",")))
    p[1] = 12
    p[2] = 2
    i = 0
    while p[i] != 99:
        p = process(p, i)
        i += 4
    print(p[0])


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
