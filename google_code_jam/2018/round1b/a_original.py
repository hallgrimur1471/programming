#!/usr/bin/env python3

from math import floor, ceil
from operator import itemgetter
from decimal import Decimal, ROUND_HALF_UP
from time import time

def main():
    start_time = time()
    T = int(input())
    for t in range(T):
        N, L = list(map(int, input().split(' ')))
        C = list(map(int, input().split(' ')))
        s = solve(N, L, C)
        print("Case #{}: {}".format(t+1, s))
    end_time = time()
    print("Calculations took {} seconds".format(end_time-start_time))

def solve(N, L, C):
    error_list = [round(100*i/N) - 100*i/N for i in range(0, N)]
    error_pos = list(map(lambda ci: error_list[ci], C))
    M = N - sum(C)
    while M > 0:
        i, mn = min(enumerate(error_pos), key=itemgetter(1))
        if mn < 0:
            C[i] += 1
            error_pos[i] = error_list[C[i] % len(error_list)]
        else:
            C.append(1)
            error_pos.append(error_list[C[-1]])
        M -= 1
    return 100+round(sum(error_pos))

def round(f):
    return int(Decimal(f).quantize(0, ROUND_HALF_UP))

main()
