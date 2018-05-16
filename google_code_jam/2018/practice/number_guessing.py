#!/usr/bin/env python3

import sys
from math import ceil

def pt(*args):
    print(*args, end='\n', flush=True)

T = int(input())
for t in range(0, T):
    A,B = map(int, input().split(' '))
    N = int(input())
    print(A, B, file=sys.stderr)
    g = 0
    while True:
        g += 1
        if g > N:
            sys.exit(1)
        m = ceil((A+B)/2)
        print("m:", m, file=sys.stderr)
        #pt(m)
        print(m, file=sys.stdout, flush=True)
        judge = input()
        print("judge:", bytes(judge, encoding="utf-8"), file=sys.stderr)
        if judge == 'TOO_SMALL':
            A = m
            continue
        elif judge == 'TOO_BIG':
            B = m-1
            continue
        elif judge == 'CORRECT':
            sys.exit(0)
        else:
            sys.exit(1)
