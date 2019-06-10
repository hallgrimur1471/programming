#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument
# pylint: disable=unused-variable
import sys
from math import inf


def solve(A, programs):
    valid_response = dict()
    valid_response["R"] = ["R", "P"]
    valid_response["P"] = ["P", "S"]
    valid_response["S"] = ["S", "R"]

    mx_len = -inf
    mx_program = None
    for i in range(len(programs)):
        if len(programs[i]) > mx_len:
            mx_len = len(programs[i])
            mx_program = programs[i]

    winning_program = []
    for i in range(mx_len):
        c = mx_program[i]
        response = valid_response[c]
        for program in programs:
            c2 = program[i % len(program)]
            response2 = valid_response[c2]
            if response == response2:
                continue
            elif set(response) & set(response2):
                response = list(set(response) & set(response2))
            else:
                return "IMPOSSIBLE"
        winning_program.append(response)
    for i, choice in enumerate(winning_program):
        if len(choice) == 1:
            winning_program[i] = choice[0]
        elif len(choice) == 2:
            winning_program[i] = choice[1]
        else:
            raise RuntimeError("something wrong!")
    programs_won = set()
    for i, c in enumerate(winning_program):
        for j, program in enumerate(programs):
            winning_response = valid_response[program[i % len(program)]][1]
            if c == winning_response:
                programs_won.add(j)
    if len(programs_won) != A:
        return "IMPOSSIBLE"

    return "".join(winning_program)


def main():
    t = int(input())
    for case_num in range(1, t + 1):
        A = int(input())
        programs = []
        for i in range(A):
            programs.append(input())
        s = solve(A, programs)
        prnt("Case #{}: {}".format(case_num, s))


def prnt(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    print(*args, **kwargs)


def dbg(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    print(*args, **kwargs)


if __name__ == "__main__":
    main()
