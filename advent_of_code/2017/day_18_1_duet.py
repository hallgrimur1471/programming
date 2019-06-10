#!/usr/bin/env python3

import sys
import time
from copy import copy, deepcopy

def main():
    start_time = time.time()

    instructions = []
    for line in sys.stdin:
        instruction = line.strip().split(' ')
        instructions.append(instruction)

    registers = dict()

    i = 0
    recovered_a_frequency = False
    last_played_frequency = None
    while not recovered_a_frequency:
        instr = instructions[i]
        op = instr[0]
        x = instr[1]

        if x not in registers:
            registers[x] = 0

        if op == "snd":
            last_played_frequency = registers[x]
        elif op == "set":
            y = val_of(instr[2], registers)
            registers[x] = y
        elif op == "add":
            y = val_of(instr[2], registers)
            registers[x] += y
        elif op == "mul":
            y = val_of(instr[2], registers)
            registers[x] *= y
        elif op == "mod":
            y = val_of(instr[2], registers)
            registers[x] %= y
        elif op == "rcv" and registers[x] != 0:
            recovered_a_frequency = True
            continue
        elif op == "jgz" and registers[x] > 0:
            y = val_of(instr[2], registers)
            i += y
            continue

        print(i, instr, "registers: ", end='')
        for register, value in registers.items():
            print(register+":"+str(value), end=' ')
        print()

        i += 1

    print(last_played_frequency)

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def val_of(v, r):
    if v.isdigit() or (v[0]=="-" and v[1:].isdigit()):
        return int(v)
    else:
        # it's a register
        return r[v]

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
