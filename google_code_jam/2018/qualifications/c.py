#!/usr/bin/env python3

import sys
from sys import stdin, stdout, stderr
from math import floor, ceil

def main():
    T = int(input())
    for t in range(T):
        A = int(input())
        solve(A)

def solve(A):
    exchanges = 0
    F = []
    for i in range(70):
        F.append([0,0,0])
    i = 1
    j = 1
    while True:
        pt("{} {}".format(i+1, j+1))
        judge = input().split(' ')
        I_ = int(judge[0])
        J_ = int(judge[1])
        exchanges += 1
        if I_ == -1 and J_ == -1:
            sys.exit(-1)
        if I_ == 0 and J_ == 0:
            return
        i_ = I_ - 1
        j_ = J_ - 1
        F[i_][j_] = 1
        if F[i-1][j-1] == 1 and F[i-1][j] == 1 and F[i-1][j+1] == 1 and (i-1)*3 < (A-9):
            i += 1

def pt(*args):
    print(*args, end='\n', flush=True)

if __name__ == "__main__":
    main()
