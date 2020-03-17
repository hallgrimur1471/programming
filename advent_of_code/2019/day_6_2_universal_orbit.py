#!/usr/bin/env python3.7
# pylint: disable=no-self-use

import sys
from collections import deque


class SpaceObject:
    def __init__(self, id_):
        self.id = id_
        self.parent = None
        self.childs = []

    def __repr__(self):
        return (
            f"SpaceObject(id={self.id}, "
            + f"parent={self.parent.id if self.parent else None}, "
            + f"childs={[child.id for child in self.childs]})"
        )


def main():
    orbit_map = []
    for line in sys.stdin:
        orbit_map.append(tuple(line.rstrip().split(")")))

    distance = find_minimum_travel_distance_between_you_and_santa_parents(
        orbit_map
    )
    print(
        f"The minimum number of orbital transfers required to "
        + f"get from the object YOU are orbiting to the object SAN is orbiting "
        + f"is {distance}"
    )


def find_minimum_travel_distance_between_you_and_santa_parents(orbit_map):
    object_map = create_object_map(orbit_map)
    you = object_map["YOU"]
    san = object_map["SAN"]

    distance = find_minimum_travel_distance_between(
        you.parent, san.parent, object_map
    )
    return distance


def find_minimum_travel_distance_between(s, t, m):
    return minimum_travel_dfs_search(s, t, m, set(), 0)


def minimum_travel_dfs_search(s, t, m, v, d):
    travel_distances = []

    if s == t:
        return d

    if s in v:
        return None

    v.add(s)
    neighbors = s.childs
    if s.parent:
        neighbors.append(s.parent)
    for neighbor in neighbors:
        travel_distance = minimum_travel_dfs_search(neighbor, t, m, v, d + 1)
        travel_distances.append(travel_distance)

    travel_distances = list(filter(None, travel_distances))

    if not travel_distances:
        return None

    minimum_travel_distance = min(travel_distances)
    return minimum_travel_distance


def determine_number_of_orbits(orbit_map):
    object_map = create_object_map(orbit_map)

    center_of_mass = object_map["COM"]

    num_orbits = 0
    objects_to_check = deque()
    objects_to_check.appendleft(center_of_mass)
    while objects_to_check:
        current_object = objects_to_check.pop()
        for child in current_object.childs:
            objects_to_check.appendleft(child)
        num_orbits += num_orbits_of_object(current_object)

    return num_orbits


def num_orbits_of_object(space_object):
    num_orbits = 0
    while space_object.parent:
        space_object = space_object.parent
        num_orbits += 1
    return num_orbits


def create_object_map(orbit_map):
    object_map = dict()
    for orbit_id_tuple in orbit_map:
        (parent, child) = get_objects(orbit_id_tuple, object_map)
        parent.childs.append(child)
        child.parent = parent
    return object_map


def get_objects(object_ids, object_map):
    return list(
        map(lambda object_id: get_object(object_id, object_map), object_ids)
    )


def get_object(object_id, object_map):
    if object_id not in object_map:
        object_ = SpaceObject(object_id)
        object_map[object_id] = object_
    else:
        object_ = object_map[object_id]
    return object_


if __name__ == "__main__":
    main()


class TestDetermineNumberOfOrbits:
    def test_correctly_determines_number_of_orbits(self):
        orbit_map = [("COM", "B"), ("B", "C"), ("B", "D")]

        num_orbits = determine_number_of_orbits(orbit_map)

        assert num_orbits == 5
