#!/usr/bin/env python3.6
import sys
import random
from collections import deque


def solve(R, C):
    visited = set()
    start_candidates = []
    for i in range(R):
        for j in range(C):
            start_candidates.append((i, j))
    random.shuffle(start_candidates)

    while start_candidates:
        pos = start_candidates.pop()
        visited.add(pos)
        path = [pos]
        if dfs(R, C, pos, visited, path):
            return True, path
    return False, None


def dfs(R, C, pos, visited, path):
    if len(path) == R * C:
        return True
    jump_candidates = []
    for i in range(R):
        for j in range(C):
            x, y = pos
            if not (
                (x == i)
                or (y == j)
                or (x - y == i - j)
                or (x + y == i + j)
                or ((i, j) in visited)
            ):
                jump_candidates.append((i, j))
    if not jump_candidates:
        return False
    random.shuffle(jump_candidates)
    while jump_candidates:
        chosen_jump = jump_candidates.pop()
        visited.add(chosen_jump)
        path.append(chosen_jump)
        if dfs(R, C, chosen_jump, visited, path):
            return True
        visited.remove(chosen_jump)
        path.pop()
    return False


def main():
    T = int(input())
    for case_num in range(1, T + 1):
        R, C = map(int, input().split(" "))
        possible, path = solve(R, C)
        if not possible:
            print("Case #{}: IMPOSSIBLE".format(case_num))
        else:
            print("Case #{}: POSSIBLE".format(case_num))
            for (i, j) in path:
                print("{} {}".format(i + 1, j + 1))


if __name__ == "__main__":
    main()
