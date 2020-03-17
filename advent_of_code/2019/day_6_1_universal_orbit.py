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

    num_orbits = determine_number_of_orbits(orbit_map)
    print(f"The total number of direct and indirect oribts is {num_orbits}")


def determine_number_of_orbits(orbit_map):
    object_map = dict()

    for orbit_id_tuple in orbit_map:
        (parent, child) = get_objects(orbit_id_tuple, object_map)
        parent.childs.append(child)
        child.parent = parent

    center_of_mass = parent
    while center_of_mass.parent:
        center_of_mass = center_of_mass.parent

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
