#!/usr/bin/env python3.7
# pylint: disable=no-self-use

from collections import deque
from dataclasses import dataclass
import logging
import itertools

import pytest


def main():
    image_data = input()

    (w, h) = (25, 6)
    answer = solve_part_2(image_data, w, h)
    for i in range(h):
        for j in range(w):
            c = answer[i * w + j]
            if c == "1":
                print("X", end="")
            elif c == "0":
                print(" ", end="")
        print()


def solve_part_1(m, w, h):
    num_layers = round(len(m) / (w * h))
    num_0_digits_in_layers = []
    for l in range(num_layers):
        num_0_digits = find_number_of_digits_in_layer(m, 0, l, w, h)
        num_0_digits_in_layers.append(num_0_digits)

    min_layer = num_0_digits_in_layers.index(min(num_0_digits_in_layers))

    num_1 = find_number_of_digits_in_layer(m, 1, min_layer, w, h)
    num_2 = find_number_of_digits_in_layer(m, 2, min_layer, w, h)
    answer = num_1 * num_2
    return answer


def solve_part_2(m, w, h):
    rendered_image = []
    for i in range(h):
        for j in range(w):
            l = 0
            while m[p(m, l, w, h, j, i)] == "2":
                l += 1
            rendered_image.append(m[p(m, l, w, h, j, i)])
    return rendered_image


def p(m, l, w, h, j, i):
    return (l * w * h) + (i * w) + j


def find_number_of_digits_in_layer(m, d, l, w, h):
    num_digits = 0
    for i in range(l * w * h, (l + 1) * w * h):
        if m[i] == str(d):
            num_digits += 1
    return num_digits


if __name__ == "__main__":
    main()

# pylint: disable=protected-access


class Test:
    def test_solve_part_1(self):
        (w, h) = (3, 2)
        image_data = "101012222221"

        answer = solve_part_1(image_data, w, h)

        assert answer == 5
