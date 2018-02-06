#!/usr/bin/env python3

"""
XOR cryptography
"""

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

def single_byte_decryption(data, num_results=1): # WIP ... pylint: disable=unused-argument
    decryption_result = DecryptionResult("data", "key")
    return decryption_result

def repeating_key_decryption(data): # pylint: disable=unused-argument
    pass
