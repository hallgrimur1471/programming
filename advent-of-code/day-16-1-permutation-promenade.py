#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    p = list(map(chr, range(ord('a'), ord('p')+1)))
    instructions = sys.stdin.read().strip().split(',')

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
