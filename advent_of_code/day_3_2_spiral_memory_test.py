#!/usr/bin/env python3

import day_3_2_spiral_memory as spiral

lens = spiral.Lens(5,5)
lens.add(1)
print(lens._array)
lens.move("right")
lens.add(0)
print(lens._array)
lens.move("up")
lens.add(0)
print(lens._array)
lens.move("left")
lens.add(0)
print(lens._array)
lens.move("left")
lens.add(0)
print(lens._array)
lens.move("down")
lens.add(0)
print(lens._array)
