#!/usr/bin/env python3

import base64
import inspect
import os.path
from statistics import mean

def repeating_key_xor(plaintext, key):
    """
    Args:
        plaintext (bytes[array])
        key (bytes[array])
    Returns:
        bytes[array]. ciphertext after applying "repeating key xor" to
        plaintext. In repeating-key XOR, you'll sequentially apply
        each byte of the key
    """
    ciphertext = bytearray(plaintext)
    for i, byte in enumerate(ciphertext):
        ciphertext[i] = byte ^ key[i%3]
    return ciphertext

def single_byte_xor_decryption(ciphertext):
    """
    Args:
        cipertext (bytes[array])
    Returns:
        list of bytes[array] with 256 elements. The elements of the list are
        inpt decrypted using every possible byte value.
    """
    candidates = bytes(range(0,256))
    results = []
    for candidate in candidates:
        result = bytearray()
        for byte in ciphertext:
            result.append(byte ^ candidate)
        results.append(result)
    return results

def sort_by_english_character_frequency(results, normalize_caps=False):
    """
    Args:
        results (list of bytes[array])
    Kwargs:
        normalize_caps (boolean): If True then all upper-case characters are
            changed to lower-case characters. Beware that this usually results
            in two equally good results, one with the message in CAPS and the
            other in lower-case. normalize_caps=True also makes this function
            considerably slower.
    Returns:
        (results, frequency_distances). results are sorted by english 
        resemblance so bytes that most likely resemble english are first.
        frequency_distances is a list of floats that corelate to results,
        lower frequency_distance means more likely to be english.
    """
    matsano_directory = os.path.dirname(os.path.realpath(__file__))

    # make a lookup table with info about english character frequency
    char_freq = dict()
    with open(os.path.join(matsano_directory,
            "character_frequency_in_english.txt")) as f:
        for line in f:
            line = line.split()
            char = line[0]
            freq = line[1]
            char_freq[char] = int(freq)
    total_chars = sum(char_freq.values())
    for k,v in char_freq.items():
        char_freq[k] = float(v)/total_chars

    # calculate score for every result, lower scores are better
    scores = []
    for result in results:
        char_scores = []
        for char, english_frequency in char_freq.items():
            if normalize_caps:
                result = bytearray(result)
                for i, byte in enumerate(result):
                    if chr(byte).isalpha():
                        result[i] = ord(chr(byte).lower())
            occurs_num = len(list(filter(lambda byte_int: byte_int==ord(char),
                    result)))
            frequency = float(occurs_num)/len(result)
            char_score = abs(frequency - english_frequency)
            char_scores.append(char_score)
        score = sum(char_scores)
        scores.append(score)

    results = list(zip(results, scores, range(0, len(results))))
    results.sort(key=lambda t: t[1], reverse=False) # sort by score
    r = [r for r,s,i in results]
    s = [s for r,s,i in results]
    i = [i for r,s,i in results]
    return r,s,i

def fixed_xor(a, b):
    """
    Args:
        a (bytes[array])
        b (bytes[array])
    Returns:
        a XOR b
    """
    return bytes([i^j for i,j in zip(a,b)])

def hex_to_base64(hx):
    """
    Args:
        hx (bytes[array])
    Returns:
        bytes[array]. base64 representation of hx
    """
    base64_bytes = base64.b64encode(hx)
    return base64_bytes
    
def hex_string_to_int(hex_string):
    """
    Args:
        hex_string (string)
    Returns:
        int. The int that the hex_string represented.
    Examples:
        'ff'  -> 255
        '0xff -> 255
    """
    return int(hex_string, 16)
