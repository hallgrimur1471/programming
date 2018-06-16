#!/usr/bin/env python3

import sys
import time
import numpy as np
import re
import math
from copy import copy, deepcopy

def main():
    mn = (0.0, math.inf)
    for i, line in enumerate(sys.stdin):
        line = line.rstrip('\n').split(', ')[2]
        line = line.lstrip('a=<')
        line = line.rstrip('>')
        line = list(map(int, line.split(',')))
        print(i, line, math.sqrt(sum([i**2 for i in line])))
        acceleration_magnitude = math.sqrt(sum([i**2 for i in line]))
        if acceleration_magnitude < mn[1]:
            mn = (i, acceleration_magnitude)
    print(mn[0], mn[1])

# Utilities
class Ut:
    up = np.array([-1,0])
    right = np.array([0,1])
    down = np.array([1,0])
    left = np.array([0,-1])
    directions = np.array([up, right, down, left])

    def rel_left(direction):
        direction_index = np.where(np.all(Ut.directions==direction, axis=1))[0]
        relative_left_index = (direction_index-1) % len(Ut.directions)
        return Ut.directions[relative_left_index][0]

    def rel_right(direction):
        direction_index = np.where(np.all(Ut.directions==direction, axis=1))[0]
        relative_right_index = (direction_index+1) % len(Ut.directions)
        return Ut.directions[relative_right_index][0]

    def is_out_of_bounds(position, map_2d):
        try:
            maybe_element = map_2d[tuple(position)]
        except IndexError:
            return True
        return False

    def get_np_string_map_from_stdin():
        smap = []
        for line in sys.stdin:
            line = line.rstrip('\n')
            smap.append(line)
        smap = np.array(list(map(list, smap)))
        return smap

    def seconds_to_hms(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("runtime: " + Ut.seconds_to_hms(end_time-start_time))
