from sys import stdin, stdout
import copy
from math import inf


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().rstrip().split(" ")))
    b = copy.copy(a)

    m = inf
    for i in reversed(range(0, n)):
        if a[i] < m:
            m = a[i]
            for j in range(0, i + 1):
                b[j] = a[i]
    print(sum(b))


if __name__ == "__main__":
    main()
