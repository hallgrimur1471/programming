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

    mx_program = max(programs, key=len)
    #dbg("mx_program:", mx_program)

    winning_program = []
    i = 0
    while programs:
        c = mx_program[i % len(mx_program)]
        response = valid_response[c]
        #dbg("response", response)
        #dbg("PROGRAMS:", programs)
        for program in programs:
            c2 = program[i % len(program)]
            response2 = valid_response[c2]
            #dbg("response2", response)
            if response == response2:
                continue
            elif set(response) & set(response2):
                response = list(set(response) & set(response2))
            else:
                return "IMPOSSIBLE"

        if len(response) == 1:
            response = response[0]
        elif len(response) == 2:
            response = response[1]
        else:
            raise RuntimeError("something wrong!")
        #dbg("final response:", response)

        remaining_programs = []
        #dbg("checking programs:", programs)
        for program in programs:
            winning_move_for_program = valid_response[program[i % len(program)]][1]
            if response == winning_move_for_program:
                continue
            remaining_programs.append(program)
        programs = remaining_programs
        #dbg("remaining programs:", programs)
        if programs:
            mx_program = max(programs, key=len)

        winning_program.append(response)
        i += 1

    if programs:
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
