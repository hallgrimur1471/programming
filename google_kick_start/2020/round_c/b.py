#!/usr/bin/env python3
import sys
from collections import deque

DEBUG = "ON"


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.childs = set()

    def __repr__(self):
        return self.ch


def dfs(node, visited):
    if node in visited:
        return None
    visited.add(node)
    max_depth = 0
    # print("node", node.ch, "has childs", list(node.childs))
    for child in node.childs:
        # print(child.ch)
        child_depth = dfs(child, visited)
        if child_depth == None:
            return None
        child_depth += 1
        max_depth = max(max_depth, child_depth)
        visited.remove(child)
    return max_depth


def get_rank(ch, node_map):
    visited = set()
    return dfs(node_map[ch], visited)


def solve(R, C, W):
    node_map = dict()
    for j in range(0, C):
        for i in range(0, R):
            ch = W[i][j]
            if ch not in node_map:
                node_map[ch] = Node(ch)
            if i < R - 1:
                ch_under = W[i + 1][j]
                if ch_under not in node_map:
                    node_map[ch_under] = Node(ch_under)
                if ch != ch_under:
                    node_map[ch].childs.add(node_map[ch_under])
    chars = [ch for ch, node in node_map.items()]
    ch_ranks = []
    for ch in chars:
        # print("processing", ch)
        # print("childs:", node_map[ch].childs)
        rank = get_rank(ch, node_map)
        if rank == None:
            return -1
        ch_ranks.append((ch, rank))
    # print("sorting")
    ch_ranks.sort(key=lambda t: t[1])
    # print(ch_ranks)
    order = [ch for ch, rank in ch_ranks]
    # print("returning")
    return "".join(order)


def main():
    sys.setrecursionlimit(10000)
    T = int(input())
    for case_num in range(1, T + 1):
        R, C = map(int, input().split(" "))
        W = []
        for _ in range(R):
            W.append(input().rstrip())
        s = solve(R, C, W)
        prnt("Case #{}: {}".format(case_num, s))


def prnt(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    print(*args, **kwargs)


def dbg(*args, **kwargs):
    if DEBUG != "ON":
        return
    if "flush" not in kwargs:
        kwargs["flush"] = True
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    print(*args, **kwargs)


if __name__ == "__main__":
    main()
