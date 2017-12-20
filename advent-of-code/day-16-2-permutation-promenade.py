#!/usr/bin/env python3

import sys
import time
from copy import copy

def main():
    start_time = time.time()

    p = list(map(chr, range(ord('a'), ord('p')+1)))
    p1 = copy(p) # before first dance
    instructions = sys.stdin.read().strip().split(',')

    # first dance
    for instruction in instructions:
        instr = instruction[0]
        if instr == 's':
            x = int(instruction[1:])
            p = p[len(p)-x:] + p[:len(p)-x]
        elif instr == 'x':
            a, b = list(map(int, instruction[1:].split('/')))
            p[a], p[b] = p[b], p[a]
        elif instr == 'p':
            a, b = instruction[1:].split('/')
            a_i = p.index(a)
            b_i = p.index(b)
            p[a_i], p[b_i] = p[b_i], p[a_i]

    p2 = copy(p) # after first dance

    # movement array
    m = ['0' for i in range(0,len(p))]
    for i in range(0, len(p)):
        m[i] = p2.index(p1[i])
    print(p1)
    print(p2)
    print(m)

    # go to million dances
    for dance in range(0, 1000000-1):
        new = copy(p)
        for i in range(0, len(p)):
            new[m[i]] = p[i]
        p = copy(new)

    p3 = copy(p) # after million dances

    # million move movement array
    m = ['0' for i in range(0,len(p))]
    for i in range(0, len(p)):
        m[i] = p3.index(p1[i])
    print()
    print(p1)
    print(p3)
    print(m)

    # go to billion dances (we need to dance the million dance 999 more times)
    for dance in range(0, 1000-1):
        new = copy(p)
        for i in range(0, len(p)):
            new[m[i]] = p[i]
        p = copy(new)

    print(''.join(p))

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
