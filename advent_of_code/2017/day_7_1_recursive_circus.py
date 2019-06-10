#!/usr/bin/env python3

import fileinput

def main():
    data = list(map(
        lambda line: list(map(
            lambda elem: elem.rstrip(','),
            line.rstrip().split(' '))),
        fileinput.input()))

    nodes = set()
    childs = set()
    for line in data:
        print(line)
        node = line[0]
        nodes.add(node)
        if len(line) > 2:
            for i in range(3, len(line)):
                childs.add(line[i])

    print(len(nodes), len(childs))
    root = nodes-childs
    print(root)

if __name__ == "__main__":
    main()
