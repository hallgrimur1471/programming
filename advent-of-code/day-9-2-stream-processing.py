#!/usr/bin/env python3

import sys

def main():
    stream = sys.stdin
    in_junk = False
    score = 0
    level = 0
    junk_chars = 0
    
    reached_end = False
    while not reached_end:
        c = stream.read(1)
        if c == '\n':
            reached_end = True
        elif c == '{' and not in_junk:
            level += 1
            score += level
        elif c == '}' and not in_junk:
            level -= 1
        elif c == '!' and in_junk:
            stream.read(1)
        elif c == '<' and not in_junk:
            in_junk = True
        elif c == '>' and in_junk:
            in_junk = False
        elif in_junk:
            junk_chars += 1
        else:
            pass

    print(score, junk_chars)

if __name__ == "__main__":
    main()
