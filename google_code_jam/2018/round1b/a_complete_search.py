#!/usr/bin/env python3

# find solution by looking at all possibilities, will suffice for test set 1

from math import floor, ceil
from operator import itemgetter
from decimal import Decimal, ROUND_HALF_UP
from time import time
from copy import copy

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
    print(legal_partitions([0,0,0], 10))
    #C.sort(reverse=True)
    #M = N
    #x = N*[0]
    #for p in legal_partitions(x, M):
    #    # find "max" p
    #    pass
    #x = N*[0]
    #M = N
    #def traverse(M, x)

def round(f):
    return int(Decimal(f).quantize(0, ROUND_HALF_UP))

def legal_partitions(x, M):
    if M == 0:
        return [x]
    r = 0
    while r < len(x)-1 and x[r] > x[r+1]:
        r += 1
    lp = [[]]
    for i in range(0, r+1):
        lp += legal_partitions(x[0:i] + [x[i]+1] + x[i+1:], M-1)
    lp = list(filter(None, lp))
    return lp

def legal_partitions_non_recursive(x, M):
    arg_stack = []
    arg_stack.append((x, M))
    while arg_stack:
        x, M = arg_stack.pop()

        if M == 0:
            return [x]
        r = 0
        while r < len(x)-1 and x[r] > x[r+1]:
            r += 1
        lp = [[]]
        escape = False
        for i in range(0, r+1):
            arg_stack.append((x[0:i] + [x[i]+1] + x[i+1:], M-1))
            escape = True
            break
            lp += legal_partitions(x[0:i] + [x[i]+1] + x[i+1:], M-1)
        lp = list(filter(None, lp))
        return lp

if __name__ == "__main__":
    print("test 1:", legal_partitions([0,0], 4))
    print("test 2:", legal_partitions([0,0,0], 4))
    print("test 3:", legal_partitions([0,0], 6))
    #lp = [list(x) for x in set(tuple(x) for x in lp)] # unique
