#!/usr/bin/env python3

import fileinput

class Tree:
    def __init__(self, root_name, root_weight):
        self.root = root_name
        self.root_weight = root_weight
        self.children = []

    def add_child(self, tree):
        self.children.append(tree)

    def weight(self):
        if self.children is None:
            return self.root_weight
        else:
            children_weight = sum([child.weight() for child in self.children])
            return self.root_weight + children_weight

def main():
    # fill weight and child map
    child_map = dict()
    weight_map = dict()
    for line in fileinput.input():
        line = line.rstrip().split(' ')
        line = list(map(lambda elem: elem.rstrip(','), line))
        node_name = line[0]
        node_weight = int(line[1].strip('()'))
        weight_map[node_name] = node_weight
        children = list(line[3:])
        child_map[node_name] = children

    root = get_global_root(child_map)
    tree = tree_from_(root, child_map, weight_map)
    find_unbalance(tree)

def tree_from_(node, child_map, weight_map):
    tree = Tree(node, weight_map[node])
    for child in child_map[node]:
        tree.add_child(tree_from_(child, child_map, weight_map))
    return tree

def find_unbalance(tree):
    weights = [subtower.weight() for subtower in tree.children]
    if all([weight == weights[0] for weight in weights]):
        for subtower in tree.children:
            find_unbalance(subtower)
    else:
        print([child.root for child in tree.children])
        print([child.root_weight for child in tree.children])
        print(weights)
        # answer was 7331-(75514-75509) = 7326
        
def get_global_root(child_map):
    nodes = set()
    childs = set()
    for node in child_map:
        nodes.add(node)
        for child in child_map[node]:
            childs.add(child)
    root = nodes-childs
    return root.pop()

if __name__ == "__main__":
    main()
