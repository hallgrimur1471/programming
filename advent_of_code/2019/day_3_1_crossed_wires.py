#!/usr/bin/env python3.7


def main():
    answer = solve()
    print(f"Distance to nearest multi-string cross section is {answer}")


def solve():
    a_route = input().split(",")
    b_route = input().split(",")

    a_visited = calculate_visited(a_route)
    b_visited = calculate_visited(b_route)

    commonly_visited = a_visited & b_visited

    nearest_cross_section_dist = find_distance_closest_to_zero(commonly_visited)
    return nearest_cross_section_dist


def calculate_visited(route):
    visited = set()
    p = (0, 0)
    for step in route:
        (direction, distance) = (step[0], int(step[1:]))
        delta = determine_delta(direction)
        while distance:
            p = add_pairs(p, delta)
            visited.add(p)
            distance -= 1
    return visited


def determine_delta(direction):
    if direction == "R":
        delta = (1, 0)
    elif direction == "L":
        delta = (-1, 0)
    elif direction == "U":
        delta = (0, 1)
    elif direction == "D":
        delta = (0, -1)
    return delta


def add_pairs(a, b):
    return (a[0] + b[0], a[1] + b[1])


def find_distance_closest_to_zero(v):
    distances = list(map(lambda t: abs(t[0]) + abs(t[1]), v))
    return min(distances)


if __name__ == "__main__":
    main()
