#!/usr/bin/env python3.5

"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

# O(n) using dict
def is_unique(s):
    k = {}
    for c in s:
        if c in k:
            return False
        k[c] = "has_occured"
    return True

print(is_unique("abcde"))
print(is_unique("abcbe"))

# if arrays and dicts are forbidden we could use double for loop O(n**2)
