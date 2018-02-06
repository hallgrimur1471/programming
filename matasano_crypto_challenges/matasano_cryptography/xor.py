#!/usr/bin/env python3

"""
XOR cryptography
"""

from matasano_cryptography.utils import DecryptionResult

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
        key with each byte of data
    """
    cipher = bytearray(data)
    for i, byte in enumerate(cipher):
        cipher[i] = byte ^ key[i%3]
    return cipher

def single_byte_decryption(ciphertext):
    """
    Args:
        cipertext (bytes[array])
    Returns:
        list of bytes[array] with 256 elements. The elements of the list are
        inpt decrypted using every possible byte value.
    """
    candidates = bytes(range(0, 256))
    results = []
    for candidate in candidates:
        result = bytearray()
        for byte in ciphertext:
            result.append(byte ^ candidate)
        results.append(result)
    return results

def single_byte_decryption(cipher, num_results=1): # WIP ... pylint: disable=unused-argument
    """
    Args:
        cipher (bytes[array]): cipher to decrypt
        num_results (int): number of results to return
    Returns:
        list of DecryptionResult, the first element is the most likely data, key
        combination according to english frequency analysis, the second element
        the second most likely etc...
        The list contains num_results elements.
    """
    key_candidates = bytes(range(0, 256))
    results = []
    for key in key_candidates:
        data = bytearray()
        for byte in cipher:
            data.append(byte ^ key)
        result = DecryptionResult(data, key)
        results.append(result)
    results.sort(key=lambda m: m.frequency_distance)
    results_to_return = results[:min(num_results, len(results))]
    return results_to_return

def repeating_key_decryption(data): # pylint: disable=unused-argument
    pass
