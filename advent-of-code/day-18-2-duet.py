#!/usr/bin/env python3

import sys
import time
import re
from copy import copy, deepcopy

class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = dict()
        self._is_waiting_for_data = False
        self.is_terminated = False
        self.num_sent_packets = 0
        self._instruction_pointer = 0
        self._instruction_register =\
                self.instructions[self._instruction_pointer]
        self._pipe = None
        self._received_values = []
        self._jumped_on_last_instruction = False

    def step(self):
        self._execute_current_instruction()
        if not (self._jumped_on_last_instruction or self._is_waiting_for_data):
            self._move_to_next_instruction()

    def set_pipe_to(self, program):
        self._pipe = program

    def receive_through_input(self, value):
        self._received_values.insert(0, value)

    def value_of_register(self, register):
        if register not in self.registers:
            self._initialize_register(register)
        return self.registers[register]

    def set_register(self, register, value):
        self.registers[register] = value

    def is_waiting_for_data(self):
        return self._received_values == [] and self._is_waiting_for_data

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
            self._send_to_pipe(self._evaluate(first_argument))
            self.num_sent_packets += 1
        elif operation == "rcv":
            if self._received_values:
                self.registers[first_argument] = self._received_values.pop()
            else:
                self._is_waiting_for_data = True
                return
        elif operation == "jgz":
            first_argument_value = self._evaluate(first_argument)
            if first_argument_value > 0:
                self._jump(second_argument_value)
                return
            else:
                pass
        elif operation == "set":
            self.registers[first_argument] = second_argument_value
        elif operation == "add":
            self.registers[first_argument] += second_argument_value
        elif operation == "mul":
            self.registers[first_argument] *= second_argument_value
        elif operation == "mod":
            self.registers[first_argument] %= second_argument_value
        self._jumped_on_last_instruction = False
        self._is_waiting_for_data = False

    def _move_to_next_instruction(self):
        self._jump(1)

    def _send_to_pipe(self, value):
        if self._pipe is None:
            error("pipe not set, can not send value")
        self._pipe.receive_through_input(value)

    def _jump(self, jump_size):
        self._instruction_pointer += jump_size
        if self._instruction_pointer_is_out_of_bounds():
            self.is_termianted = True
            return
        self._instruction_register =\
                self.instructions[self._instruction_pointer]
        self._jumped_on_last_instruction = True

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
        self.first_argument = first_argument # register
        self.second_argument = second_argument # number or register

    def len(self):
        if self.second_argument == None:
            return 2
        else:
            return 3

    def print(self):
        return (str(self.operation)+" "+str(self.first_argument)
                +" "+str(self.second_argument))

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
    A.set_pipe_to(B)
    B.set_pipe_to(A)
    deadlock = False
    finished = False
    while not (deadlock or finished):
        while not (A.is_waiting_for_data() or A.is_terminated):
            A.step()
        while not (B.is_waiting_for_data() or B.is_terminated):
            B.step()
        if A.is_waiting_for_data() and B.is_waiting_for_data():
            print("deadlock")
            deadlock = True
        if A.is_terminated and B.is_terminated:
            print("finished")
            finished = True
    print("Program B sent "+str(B.num_sent_packets)+" packets.")

def print_debug_info(msg, A, B):
    print(msg+" | A:"+str(A.registers), str(A._received_values)
                  +", B:"+str(B.registers), str(B._received_values))

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
