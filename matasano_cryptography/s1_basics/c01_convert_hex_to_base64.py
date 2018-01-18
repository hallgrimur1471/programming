#!/usr/bin/env python3

import sys
from os.path import dirname

# add matasano_cryptography package to path
crypto_parent_folder = dirname(dirname(sys.path[0]))
if crypto_parent_folder not in sys.path:
    sys.path.insert(1, crypto_parent_folder)

from matasano_cryptography import utils

def main():
    hex_string = ("49276d206b696c6c696e6720796f757220627261696e206c696b65206120"
            "706f69736f6e6f7573206d757368726f6f6d")
    hex_bytes = bytes.fromhex(hex_string)
    base64_bytes = utils.hex_to_base64(hex_bytes)
    print(base64_string.decode())
    assert base64_string.decode()==("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG"
            "9pc29ub3VzIG11c2hyb29t")

if __name__ == "__main__":
    main()
