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
    find_unbalance(tree, None, None)

def tree_from_(node, child_map, weight_map):
    tree = Tree(node, weight_map[node])
    for child in child_map[node]:
        tree.add_child(tree_from_(child, child_map, weight_map))
    return tree

def find_unbalance(tree, last_uneven_weight, last_offset):
    weights = [subtower.weight() for subtower in tree.children]
    print("subtower weights:", weights)

    # we are done if all weights equal
    if weights==[] or all([weight == weights[0] for weight in weights]):
        print("The uneven program should weigh", last_uneven_weight+last_offset)
        return

    # find the uneven child
    i = 0
    for i in range(0, len(weights)):
        if weights[i] not in (weights[:i] + weights[i+1:]):
            break
    uneven_child = tree.children[i]
    offset = (weights[:i]+weights[i+1:])[0] - uneven_child.weight()

    find_unbalance(uneven_child, uneven_child.root_weight, offset)
        
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
