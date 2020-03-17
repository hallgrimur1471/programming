#!/usr/bin/env python3.7
# pylint: disable=no-self-use

from collections import deque
from dataclasses import dataclass
import logging
import itertools
import sys
import math

import pytest


def main():
    map_string_list = read_map_string_list_from_input()
    map_ = map_string_list_2_map(map_string_list)

    num_detectable_asteroids, position = find_best_monitoring_station(map_)
    print(
        f"It's best that the monitoring station be built at {position}, "
        + f"able to detect {num_detectable_asteroids} asteroids."
    )


def find_best_monitoring_station(map_):
    h, w = find_maps_height_and_width(map_)

    max_discovered = -math.inf
    max_discovered_pos = None
    for i in range(h):
        for j in range(w):
            num_detectable_asteroids = find_num_detectable_asteroids(
                map_, i, j, h, w
            )
            if num_detectable_asteroids > max_discovered:
                max_discovered = num_detectable_asteroids
                max_discovered_pos = (i, j)

    return max_discovered_pos, max_discovered


def find_num_detectable_asteroids(m, x, y, h, w):
    num_detectable = 0
    blocked = set()

    for i in range(y, h):
        for j in range(x, w):
            num_detectable += scan(m, x, y, i, j, h, w, blocked)

    for i in reversed(range(0, y)):
        for j in reversed(range(0, x)):
            num_detectable += scan(m, x, y, i, j, h, w, blocked)

    return 0


def scan(m, x, y, i, j, h, w, blocked):
    if m[(i, j)] == "#" and (i, j) not in blocked:
        factor = 2
        return 1
    else:
        return 0


def find_maps_height_and_width(map_):
    keys = list(map_.keys())
    h = max([y for x, y in keys])
    w = max([x for x, y in keys])
    return h, w


def read_map_string_list_from_input():
    return list(map(lambda line: line.rstrip(), sys.stdin))


def map_string_list_2_map(map_string_list):
    m = dict()
    (h, w) = (len(map_string_list), len(map_string_list[0]))
    for i in range(h):
        for j in range(w):
            m[(i, j)] = map_string_list[i][j]
    return m


if __name__ == "__main__":
    main()

# pylint: disable=protected-access


class TestFindBestMonitoringStationPosition:
    def test_finds_correct_position_1(self):
        m = []
        m.append("......#.#.")
        m.append("#..#.#....")
        m.append("..#######.")
        m.append(".#.#.###..")
        m.append(".#..#.....")
        m.append("..#....#.#")
        m.append("#..#....#.")
        m.append(".##.#..###")
        m.append("##...#..#.")
        m.append(".#....####")
        m = map_string_list_2_map(m)

        num_detectable_asteroids, position = find_best_monitoring_station(m)

        assert num_detectable_asteroids == 33
        assert position == (5, 8)

    @pytest.mark.skip()
    def test_finds_correct_position_2(self):
        m = []
        m.append("#.#...#.#.")
        m.append(".###....#.")
        m.append(".#....#...")
        m.append("##.#.#.#.#")
        m.append("....#.#.#.")
        m.append(".##..###.#")
        m.append("..#...##..")
        m.append("..##....##")
        m.append("......#...")
        m.append(".####.###.")
        m = map_string_list_2_map(m)

        num_detectable_asteroids, position = find_best_monitoring_station(m)

        assert num_detectable_asteroids == 35
        assert position == (1, 2)

    @pytest.mark.skip()
    def test_finds_correct_position_3(self):
        m = []
        m.append(".#..#..###")
        m.append("####.###.#")
        m.append("....###.#.")
        m.append("..###.##.#")
        m.append("##.##.#.#.")
        m.append("....###..#")
        m.append("..#.#..#.#")
        m.append("#..#.#.###")
        m.append(".##...##.#")
        m.append(".....#.#..")
        m = map_string_list_2_map(m)

        num_detectable_asteroids, position = find_best_monitoring_station(m)

        assert num_detectable_asteroids == 41
        assert position == (6, 3)

    @pytest.mark.skip()
    def test_finds_correct_position_4(self):
        m = []
        m.append(".#..##.###...#######")
        m.append("##.############..##.")
        m.append(".#.######.########.#")
        m.append(".###.#######.####.#.")
        m.append("#####.##.#.##.###.##")
        m.append("..#####..#.#########")
        m.append("####################")
        m.append("#.####....###.#.#.##")
        m.append("##.#################")
        m.append("#####.##.###..####..")
        m.append("..######..##.#######")
        m.append("####.##.####...##..#")
        m.append(".#####..#.######.###")
        m.append("##...#.##########...")
        m.append("#.##########.#######")
        m.append(".####.#.###.###.#.##")
        m.append("....##.##.###..#####")
        m.append(".#.#.###########.###")
        m.append("#.#.#.#####.####.###")
        m.append("###.##.####.##.#..##")
        m = map_string_list_2_map(m)

        num_detectable_asteroids, position = find_best_monitoring_station(m)

        assert num_detectable_asteroids == 210
        assert position == (11, 13)
