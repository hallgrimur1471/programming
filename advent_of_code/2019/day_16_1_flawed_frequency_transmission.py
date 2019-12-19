#!/usr/bin/env python3.7
# pylint: disable=no-self-use

from collections import deque
from dataclasses import dataclass
import logging
import itertools
import sys
import math

import pytest


def main():
    signal = input()

    answer = solve_part_1(signal)

    print(f"The first eight digits of the corrected signal are {answer}")


def solve_part_1(signal):
    signal = list(signal)
    signal = list(map(int, signal))
    num_phases = 100

    corrected_signal = fft(signal, num_phases)

    corrected_signal = list(map(str, corrected_signal))
    corrected_signal = "".join(corrected_signal)
    return corrected_signal[:8]


def fft(signal, num_phases):
    for i in range(num_phases):
        print(f"Running phase {i} ...")
        signal = run_fft_phase_2(signal)
    return signal


def run_fft_phase_1(signal):
    base_pattern = [0, 1, 0, -1]

    corrected_signal = []
    for r in range(len(signal)):
        sum_ = 0
        for i, s in enumerate(signal):
            modifier = base_pattern[
                (math.floor((i + 1) / (r + 1))) % len(base_pattern)
            ]
            sum_ += modifier * s
        corrected_s = abs(sum_) % 10
        corrected_signal.append(corrected_s)

    return corrected_signal


def run_fft_phase_2(signal):
    for r in range(len(signal)):
        sum_ = 0

        jump = (r + 1) * 4
        start_i = r
        for k in range(r + 1):
            i = start_i + k
            while i < len(signal):
                sum_ += signal[i]
                i += jump

        start_i = ((r + 1) * 3) - 1
        for k in range(r + 1):
            i = start_i + k
            while i < len(signal):
                sum_ -= signal[i]
                i += jump

        signal[r] = abs(sum_) % 10

    return signal


if __name__ == "__main__":
    main()

# pylint: disable=protected-access


class TestSolvePart1:
    def test_normal_1(self):
        assert solve_part_1("80871224585914546619083218645595") == "24176176"

    def test_normal_2(self):
        assert solve_part_1("19617804207202209144916044189917") == "73745418"

    def test_normal_3(self):
        assert solve_part_1("69317163492948606335995924319873") == "52432133"


# 010x010x
#  1   5

# 001100xx001100xx
#   2       10

# 000111000xxx000111000xxx000111000xxx
#    3           1
#                5

# 4, 8, 12


# 010x010x
#    3   7

# 001100xx001100xx
#       6       1
#               4

# 000111000xxx000111000xxx000111000xxx
#          9
#
