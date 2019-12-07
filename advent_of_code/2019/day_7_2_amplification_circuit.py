#!/usr/bin/env python3.7
# pylint: disable=no-self-use

from collections import deque
from dataclasses import dataclass
import logging
import itertools

import pytest


def main():
    program = list(map(int, input().split(",")))

    max_thrust = find_max_feedback_thrust(program)
    print(
        f"The highest signal generated with feedback that "
        + f"can be sent to the thrusters is {max_thrust}"
    )


def find_max_feedback_thrust(program):
    thrusts = []
    for permutation in itertools.permutations([5, 6, 7, 8, 9]):
        thrust = find_feedback_thrust_for_permutation(program, permutation)
        thrusts.append(thrust)
    return max(thrusts)


def find_feedback_thrust_for_permutation(program, permutation):
    amplifiers = []
    for _ in range(5):
        amplifiers.append(IntcodeComputer())

    for amp in amplifiers:
        amp.load_program(program)

    for i in range(5):
        amplifier = amplifiers[i]
        phase_setting = permutation[i]
        amplifier.write_to_input(phase_setting)

    last_amplifier_output = 0  # First amplifier's input value should be 0
    last_amplifier_e_output = None
    while not any([amplifier.has_halted() for amplifier in amplifiers]):
        for i in range(5):
            amplifier = amplifiers[i]
            amplifier.write_to_input(last_amplifier_output)
            while not amplifier.is_output_available():
                amplifier.step()
                if amplifier.has_halted():
                    return last_amplifier_e_output
            amplifier_output = amplifier.read_output()
            last_amplifier_output = amplifier_output
            assert not amplifier.is_output_available()
            if i == 4:
                last_amplifier_e_output = amplifier_output


def find_max_thrust(program):
    thrusts = []
    for permutation in itertools.permutations([0, 1, 2, 3, 4]):
        thrust = find_thrust_for_permutation(program, permutation)
        thrusts.append(thrust)
    return max(thrusts)


def find_thrust_for_permutation(program, permutation):
    amplifiers = []
    for _ in range(5):
        amplifiers.append(IntcodeComputer())

    for amp in amplifiers:
        amp.load_program(program)

    last_amplifier_output = 0  # First amplifier's input value should be 0
    for i in range(5):
        amplifier = amplifiers[i]
        phase_setting = permutation[i]
        amplifier.write_to_input(phase_setting)
        amplifier.write_to_input(last_amplifier_output)
        amplifier.run()
        last_amplifier_output = amplifier.read_output()
        assert not amplifier.is_output_available()

    thrust = last_amplifier_output
    return thrust


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
            self.step()

    def step(self):
        if self._halt:
            raise RuntimeError("Can not step because computer has halted.")
        instruction = self._program_parser.parse_instruction(
            self._program, self._instruction_pointer
        )
        # print(f"Running {instruction}")
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


class TestFindMaxThrust:
    def test_finds_correct_max_thrust_1(self):
        program = list(
            map(
                int, "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")
            )
        )

        max_thrust = find_max_thrust(program)

        assert max_thrust == 43210

    def test_finds_correct_max_thrust_2(self):
        program_str = (
            "3,23,3,24,1002,24,10,24,1002,23,-1,23,"
            + "101,5,23,23,1,24,23,23,4,23,99,0,0"
        )
        program = list(map(int, program_str.split(",")))

        max_thrust = find_max_thrust(program)

        assert max_thrust == 54321

    def test_finds_correct_max_thrust_3(self):
        program_str = (
            "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,"
            + "1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        )
        program = list(map(int, program_str.split(",")))

        max_thrust = find_max_thrust(program)

        assert max_thrust == 65210


class TestFindFeedbackThrustForPermutation:
    # @pytest.mark.skip()
    def test_finds_correct_max_feedback_thrust_1(self):
        program_str = (
            "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,"
            + "27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
        )
        program = list(map(int, program_str.split(",")))

        max_thrust = find_feedback_thrust_for_permutation(
            program, [9, 8, 7, 6, 5]
        )

        assert max_thrust == 139629729

    @pytest.mark.skip()
    def test_finds_correct_max_feedback_thrust_2(self):
        program_str = (
            "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,"
            + "54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,"
            + "53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
        )
        program = list(map(int, program_str.split(",")))

        max_thrust = find_feedback_thrust_for_permutation(
            program, [9, 7, 8, 5, 6]
        )

        assert max_thrust == 18216


class TestIntcodeComputer:
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
