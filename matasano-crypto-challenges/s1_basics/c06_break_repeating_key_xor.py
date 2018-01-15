#!/usr/bin/env python3

import sys
import base64
from functools import reduce
from os.path import abspath

# matsano crypto modules
matsano_crypto_challenges = abspath("../")
sys.path.insert(1, matsano_crypto_challenges)
import utils as ut

def main():
    with open("c06_break_repeating_key_xor.in") as f:
        data = list(map(lambda line: line.rstrip(), f.readlines()))
        data = list(map(lambda line: base64.b64decode(line), data))
        data = reduce(lambda acc, elem: acc+elem, data, bytearray())
    print(data)

if __name__ == "__main__":
    main()
