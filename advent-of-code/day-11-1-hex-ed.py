#!/usr/bin/env python3

import sys

def main():
    x, y, z = 0, 0, 0
    path = sys.stdin.read().strip().split(',')

    for step in path:
        if step == "n":
            y += 1
            z += 1
        elif step == "ne":
            x += 1
            z += 1
        elif step == "se":
            x += 1
            y -= 1
        elif step == "s":
            y -= 1
            z -= 1
        elif step == "sw":
            x -= 1
            z -= 1
        elif step == "nw":
            x -= 1
            y += 1

    print(max(x,y,z))
    
if __name__ == "__main__":
    main()
