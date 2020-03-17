#!/usr/bin/env python3.7


def main():
    answer = solve()
    print(f"Minimizing signal delay, {answer} steps are required.")


def solve():
    a_route = input().split(",")
    b_route = input().split(",")

    a_travel_dict = calculate_travel_dict(a_route)
    b_travel_dict = calculate_travel_dict(b_route)

    a_visited = set(a_travel_dict.keys())
    b_visited = set(b_travel_dict.keys())

    commonly_visited = a_visited & b_visited

    steps = steps_for_minimized_signal_delay(
        a_travel_dict, b_travel_dict, commonly_visited
    )
    return steps


def calculate_travel_dict(route):
    travel_dict = dict()
    p = (0, 0)
    traveled = 0
    for step in route:
        (direction, distance) = (step[0], int(step[1:]))
        delta = determine_delta(direction)
        for _ in range(distance):
            p = add_pairs(p, delta)
            traveled += 1
            travel_dict[p] = traveled
    return travel_dict


def steps_for_minimized_signal_delay(
    a_travel_dict, b_travel_dict, cross_sections
):
    a_cross_sections_travels = [a_travel_dict[p] for p in cross_sections]
    b_cross_sections_travels = [b_travel_dict[p] for p in cross_sections]

    cross_section_travels = zip(
        a_cross_sections_travels, b_cross_sections_travels
    )

    steps = list(map(sum, cross_section_travels))
    minimal_steps = min(steps)
    return minimal_steps


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
