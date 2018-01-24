#!/usr/bin/env python3

import sys
import os.path
from os.path import dirname
from statistics import mean

# add matasano_cryptography package to path
crypto_parent_folder = dirname(dirname(sys.path[0]))
if crypto_parent_folder not in sys.path:
    sys.path.insert(1, crypto_parent_folder)

from matasano_cryptography import utils as ut
from matasano_cryptography import xor

def main():
    cipher = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c7"
            "8373e783a393b3736")
    r = xor.single_byte_decryption(cipher, num_results=3)
    print(r)
    print(r.data)
#    for i, result in enumerate(decryption_result.results()):
#        data = result.data
#        key = result.key
#        frequency_distance = result.frequency_distance
#
#        print("{:>3}. freq_dist: {:.8} | original_pos: {:>3} | text: {}".format(
#                i+1, freq_distances[i], sort_map[i], result))

#    # decode inpt using every possible character
#    results = ut.single_byte_xor_decryption(inpt)
#
#    # frequency analysis
#    results, freq_distances, sort_map = \
#            ut.sort_by_english_character_frequency(results)
#
#    # display top results
#    for i, result in enumerate(results[0:3]):
#        print("{:>3}. freq_dist: {:.8} | original_pos: {:>3} | text: {}".format(
#                i+1, freq_distances[i], sort_map[i], result))

if __name__ == "__main__":
    main()
