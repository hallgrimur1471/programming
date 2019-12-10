#!/usr/bin/env python3.7
# pylint: disable=no-self-use

from collections import deque
from dataclasses import dataclass
import logging
import itertools

import pytest


def main():
    input_ = list(map(int, input().split(",")))

    answer = solve(input_)
    print(f"{answer}")


def solve(input_):
    return None


if __name__ == "__main__":
    main()

# pylint: disable=protected-access


class Test:
    def test(self):
        pass
