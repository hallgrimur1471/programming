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

def round(f):
    return int(Decimal(f).quantize(0, ROUND_HALF_UP))

main()
