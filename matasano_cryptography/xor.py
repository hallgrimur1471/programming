#!/usr/bin/env python3

#
# xor
#

class DecryptionResult(object):
    def __init__(self):
        pass

    # todo: use properties
    #
    #   data
    #   key
    #   frequency_distance

def repeating_key_encryption(data, key):
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

def single_byte_decryption(data, num_results=1):
    decryption_result = DecryptionResult()
    return decryption_result

def repeating_key_decryption(data):
    pass
