#!/usr/bin/env python3.5

"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""

from math import floor
from copy import deepcopy

def rotate_matrix(M, cc=False):
    if len(M) != len(M[0]):
        raise RuntimeError("Only NxN matrixes are supported")
    N = len(M)
    for r in range(0, floor(N/2)):
        for k in range(r, N-r-1):
            i = r
            j = k
            tmp = M[i][j]
            for _ in range(0, 4):
                new_i, new_j = rotate_ij(i, j, N, cc)
                new_tmp = M[new_i][new_j]
                M[new_i][new_j] = tmp
                tmp = new_tmp
                i, j = new_i, new_j
    return M

def rotate_ij(i, j, N, cc):
    if cc:
        new_i = (N-1) - j
        new_j = i
    else:
        new_i = j
        new_j = (N-1) - i
    return (new_i, new_j)


m = [[1,2,3],[4,5,6],[7,8,9]]
new_m = deepcopy(m)
new_m = rotate_matrix(new_m)
for line in new_m:
    print(line)

print()
new_m = deepcopy(m)
new_m = rotate_matrix(new_m, cc=True)
for line in new_m:
    print(line)
