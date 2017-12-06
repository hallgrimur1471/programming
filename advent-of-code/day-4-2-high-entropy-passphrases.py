#!/usr/bin/env python3

import sys

valid_count = 0
for line in sys.stdin:
    word_list = line.rstrip("\n\r").split(sep=" ")
    if len(word_list) == len(set(map(''.join, list(map(sorted, word_list))))):
        valid_count += 1

print(valid_count)
