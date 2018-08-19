#!/usr/bin/env python3.5

"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

# O(n) using hash-table (Python dict)
def is_unique(s):
    k = {}
    for c in s:
        if c in k:
            return False
        k[c] = "has_occured"
    return True

# A hash-set would suite better ... (Python set)
# O(n)
def is_unique2(s):
    hs = set()
    for c in s:
        if c in hs:
            return False
        hs.add(c)
    return True

print(is_unique2("abcde"))
print(is_unique2("abcbe"))

# if lists, dicts and sets are forbidden we could use double for loop O(n**2)
