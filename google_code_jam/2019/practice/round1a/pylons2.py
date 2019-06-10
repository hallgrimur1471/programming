#!/usr/bin/env python3.6
import sys
import random
from collections import deque
from time import time


def solve(R, C, T):
    start_time = time()
    start_candidates = []
    for i in range(R):
        for j in range(C):
            start_candidates.append((i, j))
    random.shuffle(start_candidates)

    def dfs(pos, visited, path):
        if len(path) == R*C:
            return True
        jump_candidates = []
        for i in range(R):
            for j in range(C):
                x, y = pos
                if not (
                    (x == i) or
                    (y == j) or
                    (x - y == i - j) or
                    (x + y == i + j) or
                    ((i, j) in visited)
                ):
                    jump_candidates.append((i, j))
        if not jump_candidates:
            return False
        random.shuffle(jump_candidates)
        for jump in jump_candidates:
            if time() - start_time >= (0.9*(20/T)):
                return False
            visited.add(jump)
            path.append(jump)
            if dfs(jump, visited, path):
                return True
            visited.remove(jump)
            path.pop()
        return False
    
    for start_pos in start_candidates:
        visited = set([start_pos])
        path = [start_pos]
        if dfs(start_pos, visited, path):
            return True, path
    return False, None


def main():
    T = int(input())
    for case_num in range(1, T + 1):
        R, C = map(int, input().split(" "))
        possible, path = solve(R, C, T)
        if not possible:
            print("Case #{}: IMPOSSIBLE".format(case_num))
        else:
            print("Case #{}: POSSIBLE".format(case_num))
            for (i, j) in path:
                print("{} {}".format(i+1, j+1))


if __name__ == "__main__":
    main()