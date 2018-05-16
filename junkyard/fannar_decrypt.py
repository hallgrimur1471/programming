#!/usr/bin/env python3

"""
Break repeating-key XOR
"""

import base64
from functools import reduce
from os.path import dirname, join, realpath

from matasano_cryptography import xor

def main():
    root_folder = dirname(realpath(__file__))
    with open(join(root_folder, "fannar64.in")) \
            as f:
        cipher = list(map(lambda line: line.rstrip(), f.readlines()))
        cipher = ''.join(cipher)
        cipher = base64.b64decode(cipher)
        cipher = bytearray(cipher)
        #cipher = list(map(lambda line: base64.b64decode(line), cipher))
        #cipher = list(map(lambda line: bytes(line, encoding="utf-8"), cipher))
        #cipher = reduce(lambda acc, elem: acc+elem, cipher, bytearray())

    decryptionResult = xor.decrypt(cipher)
    print("\n ******** data ********\n")
    print(decryptionResult.data)
    print(" ******** key ********\n")
    print(decryptionResult.key)

if __name__ == "__main__":
    main()
