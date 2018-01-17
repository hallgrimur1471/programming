#!/usr/bin/env python3

import sys
import math
from os.path import abspath

# matsano crypto modules
matsano_crypto_challenges = abspath("../")
sys.path.insert(1, matsano_crypto_challenges)
import utils as ut

def main():
    with open("c04_detect_single_character_xor.in") as f:
        data = list(map(lambda line: line.rstrip(), f.readlines()))

    best_matches = []
    for i, line in enumerate(data):
        print("Analysing line {}/{}".format(i+1, len(data)))
        line = bytes.fromhex(line)
        decrypted = ut.single_byte_xor_decryption(line)
        decrypted, freq_dist, sort_map = \
                ut.sort_by_english_character_frequency(decrypted)
        best_matches.append((decrypted[0], freq_dist[0], sort_map[0]))
        best_matches.append((decrypted[1], freq_dist[1], sort_map[1]))

    # print best match
    best_matches.sort(key=lambda m: m[1])
    best_match = best_matches[0]
    print("Best match: freq_dist:{:.8} | char: {} | decrypted: {}".format(
            best_match[1], chr(best_match[2]), best_match[0]))

if __name__ == "__main__":
    main()
