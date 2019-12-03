#!/usr/bin/env python3.7


def main():
    answer = solve()
    print(f"Minimizing signal delay, {answer} steps are required.")


def solve():
    a_route = input().split(",")
    b_route = input().split(",")

    a_visited = calculate_visited(a_route)
    b_visited = calculate_visited(b_route)

    commonly_visited = a_visited & b_visited

    a_travel_dict = calculate_travel_dict(a_route)
    b_travel_dict = calculate_travel_dict(b_route)

    steps = steps_for_minimized_signal_delay(
        a_travel_dict, b_travel_dict, commonly_visited
    )
    return steps


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

    return set()


def calculate_travel_dict(route):
    travel_dict = dict()
    visited = set()
    p = (0, 0)
    traveled = 0
    for step in route:
        (direction, distance) = (step[0], int(step[1:]))
        delta = determine_delta(direction)
        for _ in range(distance):
            p = add_pairs(p, delta)
            # if p in travel_dict:
            #    traveled = travel_dict[p]
            # else:
            #    traveled += 1
            traveled += 1
            travel_dict[p] = traveled
            visited.add(p)
    return travel_dict


def steps_for_minimized_signal_delay(
    a_travel_dict, b_travel_dict, cross_sections
):
    # print(cross_sections)
    # print(a_travel_dict)
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
    # print(a, b)
    c = (a[0] + b[0], a[1] + b[1])
    # print(c)
    return c


def find_distance_closest_to_zero(v):
    distances = list(map(lambda t: abs(t[0]) + abs(t[1]), v))
    return min(distances)


if __name__ == "__main__":
    main()
