#!/usr/bin/env python3

import sys
import binascii
from os.path import abspath

# matsano crypto modules
matsano_crypto_challenges = abspath("../")
sys.path.insert(1, matsano_crypto_challenges)
import utils as ut

def main():
    inpt = b"Burning 'em, if you ain't quick and nimble\n" \
            + b"I go crazy when I hear a cymbal"
    key = b"ICE"
    ciphertext = ut.repeating_key_xor(inpt, key)
    print(binascii.hexlify(ciphertext).decode())

if __name__ == "__main__":
    main()
