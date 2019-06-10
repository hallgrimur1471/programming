#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument,unused-variable
# pylint: disable=inconsistent-return-statements
import sys
from collections import deque


class Node:
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.childs = []


def solve(N, W):
    root = Node("ROOT", 0)
    W = list(map(list, W))
    for w in W:
        tree = root
        while w:
            c = w.pop()
            if c in [node.char for node in tree.childs]:
                for node in tree.childs:
                    if c == node.char:
                        node.count += 1
                        tree = node
                        break
            else:
                node = Node(c, 1)
                tree.childs.append(node)
                tree = node
    return dfs(root)


def dfs(tree):
    child_matches = 0
    for child in tree.childs:
        child_matches += dfs(child)
    possible_matches_here = min(2, tree.count - child_matches)
    if possible_matches_here < 2:
        return child_matches
    return possible_matches_here + child_matches


def print_tree(tree):
    q = deque()
    q.appendleft(tree)
    line_total = 1
    line_printed = 0
    while q:
        k = q.pop()
        print((k.char, k.count), end=" ")
        line_printed += 1
        if line_printed == line_total:
            print()
            line_printed = 0
        for child in k.childs:
            q.appendleft(child)
        if line_printed == 0:
            line_total = len(q)


def main():
    T = int(input())
    for case_num in range(1, T + 1):
        N = int(input())
        W = []
        for i in range(N):
            W.append(input())
        s = solve(N, W)
        prnt("Case #{}: {}".format(case_num, s))


def prnt(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    print(*args, **kwargs)


def dbg(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    print(*args, **kwargs)


if __name__ == "__main__":
    main()
