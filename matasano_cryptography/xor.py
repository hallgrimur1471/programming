#!/usr/bin/env python3

class DecryptionResult(object):
    _CHAR_FREQ = _character_frequencies()

    def __init__(self, data, key):
        """
        Args:
            data (bytes)
            key (bytes)
        """
        self._data = data
        self._key = key
        self._frequency_distance = None

    @property
    def data(self):
        return self._data

    @property
    def key(self):
        return self._key

    @property
    def frequency_distance(self):
        if self._frequency_distance is None:
            self._frequency_distance = self._calculate_frequency_distance()
        return self._frequency_distance

    def _calculate_frequency_distance(self):
        # the lower the frequency_distance, the better
        char_scores = []
        data = self._data # copy() not requred since bytes in not mute-able
        for char, english_frequency in _CHAR_FREQ.iteritems():
            # todo: move normalize_caps to a place where it can be modified
            normalize_caps = False
            if normalize_caps:
                data = bytearray(data) # slow!
                for i, byte in enumerate(data):
                    if chr(byte).isalpha():
                        data[i] = ord(chr(byte).lower())
            occurs_num = len(list(filter(lambda byte_int: byte_int==ord(char),
                    data)))
            frequency = float(occurs_num)/len(data)
            char_score = abs(frequency - english_frequency)
            char_scores.append(char_score)
        freq_dist = sum(char_scores)
        return freq_dist

    def _character_frequencies():
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
        return char_freq

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
    decryption_result = DecryptionResult("data", "key")
    return decryption_result

def repeating_key_decryption(data):
    pass
