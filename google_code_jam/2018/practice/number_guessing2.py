from math import ceil
import sys

def pt(*args):
    print(*args, end='\n', file=sys.stdout, flush=True)

T = int(input())
for t in range(0, T):
    A,B = map(int, input().split(' '))
    N = int(input())
    for n in range(0, N):
        m = ceil((A+B)/2)
        pt(m)
        judge = input()
        if judge == 'TOO_SMALL':
            A = m
            continue
        elif judge == 'TOO_BIG':
            B = m-1
            continue
        elif judge == 'CORRECT':
            break
        else:
            sys.exit(1)