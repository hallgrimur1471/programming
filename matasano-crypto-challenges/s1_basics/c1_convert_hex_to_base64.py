#!/usr/bin/env python3

import sys
from os.path import abspath

# matsano crypto modules
matsano_crypto_challenges = abspath("../")
sys.path.insert(1, matsano_crypto_challenges)
import utils

def main():
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120"\
            + "706f69736f6e6f7573206d757368726f6f6d"
    hex_bytes = bytes.fromhex(hex_string)
    base64_bytes = utils.hex_to_base64(hex_bytes)
    base64_string = base64_bytes.decode()
    print(base64_string)

if __name__ == "__main__":
    main()
