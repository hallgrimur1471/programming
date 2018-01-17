#!/usr/bin/env python3

import sys
import os.path
from os.path import abspath
from statistics import mean

# matsano crypto modules
matsano_crypto_challenges_folder = abspath("../")
sys.path.insert(1, matsano_crypto_challenges_folder)
import utils as ut

def main():
    inpt = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d36"\
            + "3c78373e783a393b3736")

    # decode inpt using every possible character
    results = ut.single_byte_xor_decryption(inpt)

    # frequency analysis
    results, freq_distances, sort_map = \
            ut.sort_by_english_character_frequency(results)

    # display top results
    for i, result in enumerate(results[0:3]):
        print("{:>3}. freq_dist: {:.8} | original_pos: {:>3} | text: {}".format(
                i+1, freq_distances[i], sort_map[i], result))

if __name__ == "__main__":
    main()
