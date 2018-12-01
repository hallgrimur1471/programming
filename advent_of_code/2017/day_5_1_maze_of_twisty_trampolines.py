#!/usr/bin/env python3

import sys

maze = list(map(lambda x: int(str.strip(x)), sys.stdin))
i = 0
steps = 0
while i < len(maze) and i >= 0:
    if maze[i] >= 3:
        offset = -1
    else:
        offset = 1
    maze[i] += offset
    i += (maze[i]-offset)
    steps += 1
print(steps)
