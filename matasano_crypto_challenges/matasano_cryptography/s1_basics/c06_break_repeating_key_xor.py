#!/usr/bin/env python3

"""
Break repeating-key XOR test
"""

import base64
from functools import reduce
from os.path import dirname, join, realpath

from matasano_cryptography import utils as ut

def main():
    root_folder = dirname(realpath(__file__))
    with open(join(root_folder, "c06_break_repeating_key_xor.in")) \
            as f:
        data = list(map(lambda line: line.rstrip(), f.readlines()))
        data = list(map(lambda line: base64.b64decode(line), data))
        data = reduce(lambda acc, elem: acc+elem, data, bytearray())

    key = ut.break_repeating_key_xor(data)
    print(key)

if __name__ == "__main__":
    main()
