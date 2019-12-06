#!/usr/bin/env python3.7
# pylint: disable=no-self-use

from collections import deque
from dataclasses import dataclass
import logging


def main():
    program = list(map(int, input().split(",")))

    diagnostic_code = run_diagnostic_program(program)
    print(f"The diagnostic code the program produces is {diagnostic_code}")


def run_diagnostic_program(program):
    computer = IntcodeComputer()

    computer.load_program(program)
    computer.write_to_input(5)
    computer.run()

    while computer.is_output_available():
        read_output = computer.read_output()
        print(f"Read output: {read_output}")

    diagnostic_code = read_output
    return diagnostic_code


class IntcodeComputer:
    def __init__(self):
        self._instruction_pointer = 0
        self._last_instruction_pointer = 0
        self._input = deque()
        self._output = deque()
        self._halt = False
        self._program = None
        self._program_parser = ProgramParser()

    def load_program(self, program):
        self._program = program

    def run(self):
        while not self._halt:
            print("Parsing next instruction ...")
            instruction = self._program_parser.parse_instruction(
                self._program, self._instruction_pointer
            )
            print(f"Running {instruction}")
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
        elif instruction.name == "halt":
            self._run_halt_instruction(instruction)
        else:
            raise RuntimeError(f"Instruction '{instruction}' is not supported.")

    def _update_instruction_pointer(self, instruction):
        if self._instruction_pointer == self._last_instruction_pointer:
            self._instruction_pointer += len(instruction.parameters) + 1
        self._last_instruction_pointer = self._instruction_pointer

    def _run_add_instruction(self, instruction):
        first_value, second_value = self._resolve_parameters(
            instruction.parameters[0:2]
        )
        output_position = instruction.parameters[2].value

        multiplication_results = first_value + second_value
        self._program[output_position] = multiplication_results

    def _run_multiply_instruction(self, instruction):
        first_value, second_value = self._resolve_parameters(
            instruction.parameters[0:2]
        )
        output_position = instruction.parameters[2].value

        multiplication_results = first_value * second_value
        self._program[output_position] = multiplication_results

    def _run_input_instruction(self, instruction):
        input_value = self._read_input()

        write_position = instruction.parameters[0].value
        self._program[write_position] = input_value

    def _run_output_instruction(self, instruction):
        output_value = self._resolve_parameter(instruction.parameters[0])

        self._output.appendleft(output_value)

    def _run_jump_if_true_instruction(self, instruction):
        first_value = self._resolve_parameter(instruction.parameters[0])
        second_value = self._resolve_parameter(instruction.parameters[1])

        if first_value != 0:
            self._instruction_pointer = second_value

    def _run_jump_if_false_instruction(self, instruction):
        first_value = self._resolve_parameter(instruction.parameters[0])
        second_value = self._resolve_parameter(instruction.parameters[1])

        if first_value == 0:
            self._instruction_pointer = second_value

    def _run_less_than_instruction(self, instruction):
        first_value = self._resolve_parameter(instruction.parameters[0])
        second_value = self._resolve_parameter(instruction.parameters[1])
        write_position = instruction.parameters[2].value

        if first_value < second_value:
            self._program[write_position] = 1
        else:
            self._program[write_position] = 0

    def _run_equals_instruction(self, instruction):
        first_value = self._resolve_parameter(instruction.parameters[0])
        second_value = self._resolve_parameter(instruction.parameters[1])
        write_position = instruction.parameters[2].value

        if first_value == second_value:
            self._program[write_position] = 1
        else:
            self._program[write_position] = 0

    def _run_halt_instruction(self, instruction):
        self._halt = True

    def _resolve_parameters(self, parameters):
        resolved_values = list(map(self._resolve_parameter, parameters))
        return resolved_values

    def _resolve_parameter(self, parameter):
        if parameter.mode == "immediate_mode":
            return parameter.value
        elif parameter.mode == "position_mode":
            return self._program[parameter.value]

    def _read_input(self):
        read_value = self._input.pop()
        return read_value


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
            "halt": 0,
        }
        self.PARAMETER_MODE_CODE_TO_PARAMETER_MODE_NAME = {
            0: "position_mode",
            1: "immediate_mode",
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


class TestIntocdeComputer:
    computer = None

    def setup_method(self):
        self.computer = IntcodeComputer()

    def test_sucessfully_runs_multiply_program_1(self):
        program = [1002, 4, 3, 4, 33]
        self.computer.load_program(program)

        self.computer.run()

        assert self.computer._program[4] == 99

    def test_sucessfully_runs_multiply_program_2(self):
        program = [1102, 4, 3, 5, 99, 0]
        self.computer.load_program(program)

        self.computer.run()

        assert self.computer._program[5] == 12


class TestProgramParser:
    parser = None

    def setup_method(self):
        self.parser = ProgramParser()

    def test_parses_multiply_instruction_correctly(self):
        program = [1002, 4, 3, 4, 33]
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
