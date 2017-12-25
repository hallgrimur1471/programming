#!/usr/bin/env python3

import sys
import time
import numpy as np
from copy import copy, deepcopy

def main():
    letters = []
    tmap = Ut.get_np_string_map_from_stdin()
    c = '|'
    direction = Ut.down
    position = np.array([0, np.where(tmap[0]==c)[0][0]])
    path_is_complete = False
    while not path_is_complete:
        if Ut.is_out_of_bounds(position, tmap):
            path_is_complete = True
            print("out of bounds")
            break
        if c == ' ':
            path_is_complete = True
            print("end of road")
            break
        c = tmap[tuple(position)]
        if c == '+':
            found_new_direction = False
            candidates = [Ut.rel_left(direction), Ut.rel_right(direction)]
            for candidate in candidates:
                if not Ut.is_out_of_bounds(position+candidate, tmap) and\
                        tmap[tuple(position+candidate)] != ' ':
                    direction = candidate
                    found_new_direction = True
            if not found_new_direction:
                print("didn't find a new direction")
                path_is_complete = True
                break
        elif c.isalpha():
            letters.append(c)
        position += direction
        print(position, c)
    print(''.join(letters))

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
    print("runtime: "+Ut.seconds_to_hms(end_time-start_time))

#def update(m, c, p, d):
#    p[0] += d[0]
#    p[1] += d[1]
#    if p[0] < 0 or p[0] > len(m)-1:
#        return (None, None, None)
#    if p[1] < 0 or p[1] > len(m[0])-1:
#        return (None, None, None)
#    c = m[p[0]][p[1]]
#    if c == '+':
#        if d[0] == 0:
#            if p[0]-1 > 0 and m[p[0]-1][p[1]] != ' ':
#                d = (-1,0)
#            elif p[0]+1 < len(m)-1 and m[p[0]+1][p[1]] != ' ':
#                d = (1,0)
#            else:
#                return (None, None, None)
#        if d[1] == 0:
#            if p[1]-1 > 0 and m[p[0]][p[1]-1] != ' ':
#                d = (0,-1)
#            if p[1]+1 < len(m[0]-1) and m[p[0]][p[1]+1]:
#                d = (0,1)
#            else:
#                return (None, None, None)
#    elif c == ' ':
#        return (None, None, None)
#
#    c = '|'
#    pos = [tube_map[0].index(c), 0]
#    print(pos, c)
#    direction = (0,1)
#    while True:
#        if ((direction == (0,1)  and pos[1] == len(tube_map)-1 and c != '+') or
#            (direction == (0,-1) and pos[1] == 0 and c != '+') or
#            (direction == (-1,0) and pos[0] == 0 and c != '+') or
#            (direction == (1,0)  and pos[0] == len(tube_map)-1 and c != '+')):
#            break
#        pos[0] = pos[0]+direction[0]
#        pos[1] = pos[1]+direction[1]
#        c = tube_map[pos[0]][pos[1]]
#        print(pos, c)
#        if c == '+':
#            if direction[1] == 0:
#                if pos[1] != 0 and tube_map[pos[0]][pos[1]-1] != ' ':
#                    direction = (0,-1)
#                elif pos[1] != len(tube_map)-1 and tube_map[pos[0]][pos[1]+1] != ' ':
#                    direction = (0,1)
#                else:
#                    error("dir1")
#            elif direction[0] == 1:
#                if pos[0] != 0 and tube_map[pos[0]-1][pos[1]] != ' ':
#                    direction = (-1,0)
#                elif pos[0] != len(tube_map[0])-1 and tube_map[pos[0]+1][pos[1]] != ' ':
#                    direction = (1,0)
#        elif c.isalpha():
#            letters.append(c)
#        elif c == ' ':
#            break
#        else:
#            pass
#    print(letters)
