#!/usr/bin/env python3

"""
Fixed XOR test
"""

import sys
from os.path import dirname
import binascii

# add matasano_cryptography package to path
crypto_parent_folder = dirname(dirname(sys.path[0]))
if crypto_parent_folder not in sys.path:
    sys.path.insert(1, crypto_parent_folder)

# pylint: disable=wrong-import-position
from matasano_cryptography import utils

## matsano crypto modules
#matsano_crypto_challenges = abspath("../")
#sys.path.insert(1, matsano_crypto_challenges)
#import utils

def main():
    data1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    data2 = bytes.fromhex("686974207468652062756c6c277320657965")
    data_xor = utils.fixed_xor(data1, data2)
    print(binascii.hexlify(data_xor).decode())
    assert (binascii.hexlify(data_xor).decode()
            == "746865206b696420646f6e277420706c6179")

if __name__ == "__main__":
    main()
