#!/usr/bin/env python3.7
# pylint: disable=no-self-use

from collections import deque
from dataclasses import dataclass
import logging
import itertools
import copy
import time

import pytest


def main():
    program = program_list_2_dict(list(map(int, input().split(","))))

    boost_keycode = find_boost_keycode(program)

    print(f"The BOOST keycode is {boost_keycode}")


def find_boost_keycode(program):
    computer = IntcodeComputer()
    computer.load_program(program)
    computer.write_to_input(1)
    computer.run()
    return computer.read_output()


class IntcodeComputer:
    def __init__(self):
        self._instruction_pointer = 0
        self._last_instruction_pointer = 0
        self._relative_base = 0
        self._input = deque()
        self._output = deque()
        self._halt = False
        self._program = None
        self._program_parser = ProgramParser()

    def load_program(self, program):
        self._program = copy.copy(program)

    def run(self):
        while not self._halt:
            self.step()

    def step(self):
        if self._halt:
            raise RuntimeError("Can not step because computer has halted.")
        instruction = self._program_parser.parse_instruction(
            self._program, self._instruction_pointer
        )
        self._run_instruction(instruction)
        self._update_instruction_pointer(instruction)

    def write_to_input(self, input_value):
        self._input.appendleft(input_value)

    def is_output_available(self):
        if self._output:
            return True
        return False

    def read_output(self):
        read_value = self._output.pop()
        return read_value

    def has_halted(self):
        return self._halt

    def _run_instruction(self, instruction):
        if instruction.name == "add":
            self._run_add_instruction(instruction)
        elif instruction.name == "multiply":
            self._run_multiply_instruction(instruction)
        elif instruction.name == "input":
            self._run_input_instruction(instruction)
        elif instruction.name == "output":
            self._run_output_instruction(instruction)
        elif instruction.name == "jump_if_true":
            self._run_jump_if_true_instruction(instruction)
        elif instruction.name == "jump_if_false":
            self._run_jump_if_false_instruction(instruction)
        elif instruction.name == "less_than":
            self._run_less_than_instruction(instruction)
        elif instruction.name == "equals":
            self._run_equals_instruction(instruction)
        elif instruction.name == "relative_base_offset":
            self._run_relative_base_offset_instruction(instruction)
        elif instruction.name == "halt":
            self._run_halt_instruction(instruction)
        else:
            raise RuntimeError(f"Instruction '{instruction}' is not supported.")

    def _update_instruction_pointer(self, instruction):
        if self._instruction_pointer == self._last_instruction_pointer:
            self._instruction_pointer += len(instruction.parameters) + 1
        self._last_instruction_pointer = self._instruction_pointer

    def _run_add_instruction(self, instruction):
        first_value, second_value = self._resolve_read_parameters(
            instruction.parameters[0:2]
        )
        write_address = self._resolve_write_parameter(instruction.parameters[2])

        multiplication_results = first_value + second_value
        self._set_memory(write_address, multiplication_results)

    def _run_multiply_instruction(self, instruction):
        first_value, second_value = self._resolve_read_parameters(
            instruction.parameters[0:2]
        )
        write_address = self._resolve_write_parameter(instruction.parameters[2])

        multiplication_results = first_value * second_value
        self._set_memory(write_address, multiplication_results)

    def _run_input_instruction(self, instruction):
        input_value = self._read_input()

        write_address = self._resolve_write_parameter(instruction.parameters[0])
        self._set_memory(write_address, input_value)

    def _run_output_instruction(self, instruction):
        output_value = self._resolve_read_parameter(instruction.parameters[0])

        self._output.appendleft(output_value)

    def _run_jump_if_true_instruction(self, instruction):
        first_value = self._resolve_read_parameter(instruction.parameters[0])
        second_value = self._resolve_read_parameter(instruction.parameters[1])

        if first_value != 0:
            self._instruction_pointer = second_value

    def _run_jump_if_false_instruction(self, instruction):
        first_value = self._resolve_read_parameter(instruction.parameters[0])
        second_value = self._resolve_read_parameter(instruction.parameters[1])

        if first_value == 0:
            self._instruction_pointer = second_value

    def _run_less_than_instruction(self, instruction):
        first_value = self._resolve_read_parameter(instruction.parameters[0])
        second_value = self._resolve_read_parameter(instruction.parameters[1])
        write_address = self._resolve_write_parameter(instruction.parameters[2])

        if first_value < second_value:
            self._set_memory(write_address, 1)
        else:
            self._set_memory(write_address, 0)

    def _run_equals_instruction(self, instruction):
        first_value = self._resolve_read_parameter(instruction.parameters[0])
        second_value = self._resolve_read_parameter(instruction.parameters[1])
        write_address = self._resolve_write_parameter(instruction.parameters[2])

        if first_value == second_value:
            self._set_memory(write_address, 1)
        else:
            self._set_memory(write_address, 0)

    def _run_relative_base_offset_instruction(self, instruction):
        value = self._resolve_read_parameter(instruction.parameters[0])
        self._relative_base += value

    def _run_halt_instruction(self, instruction):
        self._halt = True

    def _resolve_read_parameters(self, parameters):
        resolved_values = list(map(self._resolve_read_parameter, parameters))
        return resolved_values

    def _resolve_read_parameter(self, parameter):
        if parameter.mode == "immediate_mode":
            return parameter.value
        elif parameter.mode == "position_mode":
            return self._get_memory(parameter.value)
        elif parameter.mode == "relative_mode":
            return self._get_memory(self._relative_base + parameter.value)

    def _resolve_write_parameter(self, parameter):
        if parameter.mode == "position_mode":
            write_address = parameter.value
        elif parameter.mode == "relative_mode":
            write_address = parameter.value + self._relative_base
        else:
            raise RuntimeError("Unsupported input parameter mode")
        return write_address

    def _read_input(self):
        read_value = self._input.pop()
        return read_value

    def _set_memory(self, address, value):
        self._program[address] = value

    def _get_memory(self, address):
        try:
            return self._program[address]
        except KeyError:
            return 0


class ProgramParser:
    def __init__(self):
        self.NUM_TO_INSTRUCTION_NAME = {
            1: "add",
            2: "multiply",
            3: "input",
            4: "output",
            5: "jump_if_true",
            6: "jump_if_false",
            7: "less_than",
            8: "equals",
            9: "relative_base_offset",
            99: "halt",
        }
        self.INSTRUCTION_NAME_TO_NUMBER_OF_PARAMETERS = {
            "add": 3,
            "multiply": 3,
            "input": 1,
            "output": 1,
            "jump_if_true": 2,
            "jump_if_false": 2,
            "less_than": 3,
            "equals": 3,
            "relative_base_offset": 1,
            "halt": 0,
        }
        self.PARAMETER_MODE_CODE_TO_PARAMETER_MODE_NAME = {
            0: "position_mode",
            1: "immediate_mode",
            2: "relative_mode",
        }

    def parse_instruction(self, program, instruction_pointer):
        instruction_name = self._parse_current_instruction_name(
            program, instruction_pointer
        )
        parameter_modes = self._parse_current_parameter_modes(
            program, instruction_pointer, instruction_name
        )
        parameters = self._parse_current_parameters(
            program, instruction_pointer, instruction_name
        )
        self._set_parameter_modes(parameters, parameter_modes)

        instruction = Instruction(name=instruction_name, parameters=parameters)
        return instruction

    def _parse_current_instruction_name(self, program, instruction_pointer):

        instruction_info_cunk = str(program[instruction_pointer])

        instruction_part = instruction_info_cunk[-2:]
        instruction = self.NUM_TO_INSTRUCTION_NAME[int(instruction_part)]

        return instruction

    def _parse_current_parameter_modes(
        self, program, instruction_pointer, instruction_name
    ):
        number_of_parameters = self.INSTRUCTION_NAME_TO_NUMBER_OF_PARAMETERS[
            instruction_name
        ]

        instruction_info_cunk = str(program[instruction_pointer])
        parameter_modes_part = instruction_info_cunk[0:-2].zfill(
            number_of_parameters
        )

        parameter_modes = dict()
        for i, mode_str in enumerate(reversed(parameter_modes_part)):
            parameter_modes[i] = int(mode_str)

        return parameter_modes

    def _parse_current_parameters(
        self, program, instruction_pointer, instruction_name
    ):
        number_of_parameters = self.INSTRUCTION_NAME_TO_NUMBER_OF_PARAMETERS[
            instruction_name
        ]

        parameters = []
        for i in range(number_of_parameters):
            parameter_value = program[instruction_pointer + 1 + i]
            parameter = Parameter(value=parameter_value, mode=None)
            parameters.append(parameter)
        return parameters

    def _set_parameter_modes(self, parameters, parameter_modes):
        for i, parameter in enumerate(parameters):
            parameter_mode_code = parameter_modes[i]
            param_mode_name = self.PARAMETER_MODE_CODE_TO_PARAMETER_MODE_NAME[
                parameter_mode_code
            ]
            parameter.mode = param_mode_name


def program_list_2_dict(program_list):
    program_dict = dict()
    for i in range(len(program_list)):
        program_dict[i] = program_list[i]
    return program_dict


@dataclass
class Instruction:
    name: str
    parameters: list


@dataclass
class Parameter:
    value: int
    mode: str


if __name__ == "__main__":
    main()

# pylint: disable=protected-access


class TestProgramList2Dict:
    def test_converts_correctly(self):
        program_list = [2, 8, 1002, 4]

        program_dict = program_list_2_dict(program_list)

        assert program_dict[0] == 2
        assert program_dict[1] == 8
        assert program_dict[2] == 1002
        assert program_dict[3] == 4
        assert len(program_dict.items()) == 4


def test_quine():
    program_str = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    program_list = list(map(int, program_str.split(",")))
    program = program_list_2_dict(program_list)

    computer = IntcodeComputer()
    computer.load_program(program)
    computer.run()
    computer_output = []
    while computer.is_output_available():
        computer_output.append(computer.read_output())
    assert computer_output == program_list


def test_produces_16_digit_number():
    program_str = "1102,34915192,34915192,7,4,7,99,0"
    program_list = list(map(int, program_str.split(",")))
    program = program_list_2_dict(program_list)

    computer = IntcodeComputer()
    computer.load_program(program)
    computer.run()

    assert len(str((computer.read_output()))) == 16


def test_outputs_the_large_number_in_the_middle():
    program_str = "104,1125899906842624,99"
    program_list = list(map(int, program_str.split(",")))
    program = program_list_2_dict(program_list)

    computer = IntcodeComputer()
    computer.load_program(program)
    computer.run()

    assert computer.read_output() == 1125899906842624


class TestIntcodeComputer:
    computer = None

    def setup_method(self):
        self.computer = IntcodeComputer()

    def test_sucessfully_runs_multiply_program_1(self):
        program = program_list_2_dict([1002, 4, 3, 4, 33])
        self.computer.load_program(program)

        self.computer.run()

        assert self.computer._program[4] == 99

    def test_sucessfully_runs_multiply_program_2(self):
        program = program_list_2_dict([1102, 4, 3, 5, 99, 0])
        self.computer.load_program(program)

        self.computer.run()

        assert self.computer._program[5] == 12


class TestProgramParser:
    parser = None

    def setup_method(self):
        self.parser = ProgramParser()

    def test_parses_multiply_instruction_correctly(self):
        program = program_list_2_dict([1002, 4, 3, 4, 33])
        instruction_pointer = 0

        instruction = self.parser.parse_instruction(
            program, instruction_pointer
        )

        assert instruction.name == "multiply"
        assert len(instruction.parameters) == 3
        assert instruction.parameters[0].value == 4
        assert instruction.parameters[1].value == 3
        assert instruction.parameters[2].value == 4
        assert instruction.parameters[0].mode == "position_mode"
        assert instruction.parameters[1].mode == "immediate_mode"
        assert instruction.parameters[2].mode == "position_mode"
