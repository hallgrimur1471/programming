#!/usr/bin/env python3

import sys
import binascii
from os.path import dirname

# add matasano_cryptography package to path
crypto_parent_folder = dirname(dirname(sys.path[0]))
if crypto_parent_folder not in sys.path:
    sys.path.insert(1, crypto_parent_folder)

from matasano_cryptography import repeating_key_xor

def main():
    data = b"Burning 'em, if you ain't quick and nimble\n" \
            + b"I go crazy when I hear a cymbal"
    key = b"ICE"

    cipher = repeating_key_xor.encrypt(data, key)
    ciphertext = binascii.hexlify(cipher).decode()
    print(ciphertext)

    assert ciphertext==("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d6334"
            "3c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c"
            "692b20283165286326302e27282f")

if __name__ == "__main__":
    main()
