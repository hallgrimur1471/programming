#!/usr/bin/env python3

import sys
from os.path import abspath
import binascii

# matsano crypto modules
matsano_crypto_challenges = abspath("../")
sys.path.insert(1, matsano_crypto_challenges)
import utils

def main():
    in1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    in2 = bytes.fromhex("686974207468652062756c6c277320657965")
    result = utils.fixed_xor(in1, in2)
    print(binascii.hexlify(result).decode())

if __name__ == "__main__":
    main()
