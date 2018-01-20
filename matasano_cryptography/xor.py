#!/usr/bin/env python3

"""
XOR cryptography
"""

import sys
import os
from os.path import dirname

class DecryptionResult(object):
    """
    Class to store results of a decryption, calculates it's likeness to english.
    """

    def __init__(self, data, key):
        """
        Args:
            data (bytes)
            key (bytes)
        """
        self._data = data
        self._key = key
        self._freq_dist = None # frequency distance
        self._english_char_freq = None # english character frequencies

    @property
    def data(self):
        return self._data

    @property
    def key(self):
        return self._key

    @property
    def frequency_distance(self):
        if self._freq_dist is None:
            self._freq_dist = self._calculate_freq_dist()
        return self._freq_dist

    def _calculate_freq_dist(self):
        """
        Returns:
            freq_dist (float). A score specifying likeness of self.data
            and typical english sentences. The lower the value of freq_dist
            the more similar self.data is to english.
        """
        if self._english_char_freq is None:
            self._english_char_freq = self._calculate_english_char_freq()
        # the lower the frequency_distance, the better
        char_scores = []
        data = self._data # copy() not requred since bytes in not mute-able
        for char, engish_freq in self._english_char_freq.iteritems():
            # todo: move normalize_caps to a place where it can be modified
            normalize_caps = False
            if normalize_caps:
                data = bytearray(data) # slow!
                for i, byte in enumerate(data):
                    if chr(byte).isalpha():
                        data[i] = ord(chr(byte).lower())
            occurs_num = len([byte for byte in data if byte == ord(char)])
            frequency = float(occurs_num)/len(data)
            char_score = abs(frequency - engish_freq)
            char_scores.append(char_score)
        freq_dist = sum(char_scores)
        return freq_dist

    def _calculate_english_char_freq(self):
        """
        Returns:
            char_freq (dict). Dictionary where:
                key: english character
                value: percentage specifying how common the character is
                       in english.
        """
        # make a lookup table with info about english character frequency
        char_freq = dict()
        matasano_directory = dirname(sys.path[0])
        with open(os.path.join(matasano_directory,
                               "character_frequency_in_english.txt")) as f:
            for line in f:
                line = line.split()
                char = line[0]
                freq = line[1]
                char_freq[char] = int(freq)
        total_chars = sum(char_freq.values())
        for k, v in char_freq.items():
            char_freq[k] = float(v)/total_chars
        return char_freq

def repeating_key_encryption(data, key): # pylint: disable=unused-argument
    pass

def encrypt(data, key):
    """
    Args:
        data (bytes[array])
        key (bytes[array])
    Returns:
        cipher (bytes[array]) after applying repeating key xor encryption to
        data. In repeating key XOR, you'll sequentially XOR each byte of the
        key with every byte of data
    """
    cipher = bytearray(data)
    for i, byte in enumerate(cipher):
        cipher[i] = byte ^ key[i%3]
    return cipher

def single_byte_decryption(data, num_results=1): # WIP ... pylint: disable=unused-argument
    decryption_result = DecryptionResult("data", "key")
    return decryption_result

def repeating_key_decryption(data): # pylint: disable=unused-argument
    pass
