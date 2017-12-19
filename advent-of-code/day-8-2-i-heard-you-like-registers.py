#!/usr/bin/env python3

import sys
import math

def main():
    registers = dict()
    highest = -math.inf
    for line in sys.stdin:
        line = line.strip().split(' ')

        instr_reg = line[0]
        instr_op = line[1]
        instr_val = int(line[2])
        cond_reg = line[4]
        cond_op = line[5]
        cond_val = int(line[6])

        if instr_reg not in registers:
            registers[instr_reg] = 0
        if cond_reg not in registers:
            registers[cond_reg] = 0

        cond_is_true = check_cond(cond_reg, cond_op, cond_val, registers)
        
        if cond_is_true:
            run_instr(instr_reg, instr_op, instr_val, registers)
            highest = max(highest, registers[instr_reg])

    print(highest)

def check_cond(reg, op, val, registers):
    reg_val = registers[reg]

    if op == '>':
        return reg_val > val
    elif op == '>=':
        return reg_val >= val
    elif op == '==':
        return reg_val == val
    elif op == '!=':
        return reg_val != val
    elif op == '<=':
        return reg_val <= val
    elif op == '<':
        return reg_val < val

def run_instr(reg, op, val, registers):
    if op == 'inc':
        registers[reg] += val
    elif op == 'dec':
        registers[reg] -= val
    else:
        error("run_instr")

def error(msg):
    sys.stderr.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
