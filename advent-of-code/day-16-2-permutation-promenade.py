#!/usr/bin/env python3

import sys
import time
from copy import copy

def main():
    start_time = time.time()

    num_dances = 1000000000
    p = list(map(chr, range(ord('a'), ord('p')+1)))
    p1 = copy(p) # before first dance
    instructions = sys.stdin.read().strip().split(',')

    history = []
    dance_num = 0
    found_loop = False
    while dance_num < num_dances:
        history.append(copy(p))

        if dance_num % 100 == 0:
            print(dance_num, seconds_to_hms(time.time()-start_time),
                ''.join(p))

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

        dance_num += 1

        if p in history and found_loop == False:
            loop_size = dance_num
            print("found loop!: ", loop_size)
            found_loop = True
            while dance_num < num_dances:
                dance_num += loop_size 
            dance_num -= loop_size
            print("dance_num increased to: "+str(dance_num))

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
