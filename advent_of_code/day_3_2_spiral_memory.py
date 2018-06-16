#!/usr/bin/env python3

import numpy as np
import sys
import math
import time

class Lens:
    def __init__(self, width, height):
        if width != height:
            error("width and height must be equal")
        if width % 2 != 1:
            error("width and height must be odd integers")
        self._width = width
        self._height = height
        self._array = np.zeros((width, height), dtype=np.int)
        self._mid = math.floor(width/2)

    def add(self, num):
        self._array[self._mid][self._mid] = num + self._neighbours()

    def move(self, direction):
        if direction == "left":
            self._insert_zeros_at_column(0)
            self._delete_column_at(self._width)
        if direction == "right":
            self._insert_zeros_at_column(self._width)
            self._delete_column_at(0)
        if direction == "up":
            self._insert_zeros_at_row(0)
            self._delete_row_at(self._height)
        if direction == "down":
            self._insert_zeros_at_row(self._height)
            self._delete_row_at(0)

    def get_cursor_value(self):
        return self._array[self._mid][self._mid]

    def _insert_zeros_at_column(self, row):
        self._array = np.insert(self._array, row, 0, axis=1)

    def _delete_column_at(self, row):
        self._array = np.delete(self._array, row, axis=1)

    def _insert_zeros_at_row(self, column):
        self._array = np.insert(self._array, column, 0, axis=0)

    def _delete_row_at(self, column):
        self._array = np.delete(self._array, column, axis=0)

    def _neighbours(self):
        a = self._array
        m = self._mid
        return (sum(a[m-1][m-1:m+2])
               +sum(a[m+1][m-1:m+2])
               +sum(a[m][[m-1, m+1]]))

def error(msg):
     sys.stderr.write(msg) 
     sys.exit(1)

def get_next_direction(pos):
    x = pos[0]
    y = pos[1]
    N = max(abs(x), abs(y))
    if x == N and y > -N and y < N:
        return ("up", (x, y+1))
    elif y == N and x > -N:
        return ("left", (x-1, y))
    elif x == -N and y > -N:
        return ("down", (x, y-1))
    else:
        return ("right", (x+1, y))

def main():
    lens = Lens(21, 21)
    lens.add(1)
    position = (0,0)
    print(lens._array)

    current_value = lens.get_cursor_value()
    while current_value < 312051:
        direction, position = get_next_direction(position)
        lens.move(direction)
        lens.add(0)
        current_value = lens.get_cursor_value()
        print(lens._array, position)
        time.sleep(0.2)

if __name__ == "__main__":
    main()


