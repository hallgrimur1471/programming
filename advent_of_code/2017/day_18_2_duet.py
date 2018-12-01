#!/usr/bin/env python3

import sys
import time
import re
from copy import copy, deepcopy

class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = dict()
        self.is_terminated = False
        self.num_sent_packets = 0
        self._instruction_pointer = 0
        self._instruction_register =\
                self.instructions[self._instruction_pointer]
        self._pipe_in = []
        self._pipe_out = []
        self._jumped_on_last_instruction = False

    def step(self):
        self._jumped_on_last_instruction = False # reset
        self._execute_current_instruction()
        if not (self._jumped_on_last_instruction or self.is_waiting_for_data()):
            self._move_to_next_instruction()

    def pipe_output_to(self, program):
        if not isinstance(program, Program):
            error("pipe_output_to can only pipe to another program")
        self._pipe_out = program._pipe_in

    def set_register(self, register, value):
        self.registers[register] = value

    def is_waiting_for_data(self):
        return (len(self._pipe_in) == 0 and
                self._instruction_register.operation== "rcv")

    def _execute_current_instruction(self):
        instruction = self._instruction_register
        operation = instruction.operation
        first_argument = instruction.first_argument
        if instruction.len() == 3:
            second_argument = instruction.second_argument
            second_argument_value = self._evaluate(second_argument)
        if first_argument.isalpha() and first_argument not in self.registers:
            self._initialize_register(first_argument)
        if operation == "snd":
            self._send_value(self._evaluate(first_argument))
            self.num_sent_packets += 1
        elif operation == "rcv":
            if len(self._pipe_in) > 0:
                self.registers[first_argument] = self._pipe_in.pop()
        elif operation == "jgz":
            first_argument_value = self._evaluate(first_argument)
            if first_argument_value > 0:
                self._jump(second_argument_value)
                self._jumped_on_last_instruction = True
        elif operation == "set":
            self.registers[first_argument] = second_argument_value
        elif operation == "add":
            self.registers[first_argument] += second_argument_value
        elif operation == "mul":
            self.registers[first_argument] *= second_argument_value
        elif operation == "mod":
            self.registers[first_argument] %= second_argument_value

    def _send_value(self, value):
        self._pipe_out.insert(0, value)

    def _move_to_next_instruction(self):
        self._jump(1)

    def _jump(self, jump_size):
        self._instruction_pointer += jump_size
        if self._instruction_pointer_is_out_of_bounds():
            self.is_terminated = True
            return
        self._instruction_register =\
                self.instructions[self._instruction_pointer]

    def _instruction_pointer_is_out_of_bounds(self):
        return (self._instruction_pointer < 0 or 
                self._instruction_pointer > len(self.instructions)-1)

    def _evaluate(self, expression):
        # expression must be a string
        if not isinstance(expression, str):
            error("_evaluate only supports strings")
        # expression is either a number_string or a single letter register
        if re.match(r"[-+]?\d+$", expression) is not None:
            # expression is a number string
            return int(expression)
        if len(expression) != 1:
            error("_evalute only supports single letter registers")
        # expression is a single letter register
        return self.registers[expression]

    def _initialize_register(self, register):
        self.registers[register] = 0

class Instruction:
    def __init__(self, operation, first_argument, second_argument=None):
        self.operation = operation
        self.first_argument = first_argument
        self.second_argument = second_argument

    def len(self):
        if self.second_argument == None:
            return 2
        else:
            return 3

    def to_str(self):
        return " ".join(map(str, [self.operation, self.first_argument,
                self.second_argument]))

def main():
    start_time = time.time()
    instructions = []
    for line in sys.stdin:
        elems = line.strip().split(' ')
        if len(elems) == 2:
            instruction = Instruction(elems[0], elems[1])
        elif len(elems) == 3:
            instruction = Instruction(elems[0], elems[1], elems[2])
        else:
            error("invalid instruction length")
        instructions.append(instruction)
    A = Program(instructions)
    B = Program(instructions)
    A.set_register('p', 0)
    B.set_register('p', 1)
    A.pipe_output_to(B)
    B.pipe_output_to(A)
    while not deadlock(A, B):
        while not (A.is_waiting_for_data() or A.is_terminated):
            A.step()
        while not (B.is_waiting_for_data() or B.is_terminated):
            B.step()
    print("Program B sent "+str(B.num_sent_packets)+" packets.")

def deadlock(A, B):
    return ((A.is_waiting_for_data() or A.is_terminated) and
            (B.is_waiting_for_data() or B.is_terminated))

def print_debug_info(msg, A, B):
    print(msg+" | A:"+str(A.registers), "str(A._pipe_in)"
                  +", B:"+str(B.registers), "str(B._pipe_in)")

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
