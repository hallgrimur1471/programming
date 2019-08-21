#!/usr/bin/env python3.7

import random


def rand_char():
    c1 = ord("a")
    c2 = ord("z")
    return chr(random.randint(c1, c2))


while True:
    for _ in range(35):
        if random.randint(0, 10):
            print(
                "".join([rand_char() for _ in range(3)])
                + str(random.randint(10, 99))
            )
        else:
            print(
                "".join([rand_char() for _ in range(4)])
                + str(random.randint(10, 99))
            )
    input()
