#!/usr/bin/env python3.6
import random


def solve(R, C):
    if max(R, C) <= 3 or (R, C) == (2, 4) or (R, C) == (4, 2):
        return []
    start_candidates = [(i, j) for i in range(R) for j in range(C)]
    sol_found = False
    while not sol_found:
        path = []
        visited = set()
        jump_candidates = start_candidates
        while True:
            jump = random.choice(jump_candidates)
            visited.add(jump)
            path.append(jump)
            if len(path) == R * C:
                sol_found = True
                break
            jump_candidates = []
            for i in range(R):
                for j in range(C):
                    x, y = path[-1]
                    if not (
                        (x == i)
                        or (y == j)
                        or (x - y == i - j)
                        or (x + y == i + j)
                        or ((i, j) in visited)
                    ):
                        jump_candidates.append((i, j))
            if not jump_candidates:
                break
    return path


def main():
    T = int(input())
    for case_num in range(1, T + 1):
        R, C = map(int, input().split(" "))
        sol = solve(R, C)
        print(
            "Case #{}: {}".format(case_num, "POSSIBLE" if sol else "IMPOSSIBLE")
        )
        if sol:
            for (i, j) in sol:
                print("{} {}".format(i + 1, j + 1))


if __name__ == "__main__":
    main()
