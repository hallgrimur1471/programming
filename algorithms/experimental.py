#!/usr/bin/env python3

class Node:
    def __init__(self, name, val=None):
        self.name = name
        self.val = val
        self.childs = []
        self.parents = []

class Edge:
    def __init__(self, u, v, val):
        self.u = u
        self.v = v
        self.val = val

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, u, v, val):
        self.edges.append(Edge(u, v, val))

    def getEdge(self, u, v):
        for edge in self.edges:
            pass

graph = Graph()
graph.addNode(Node('s'))
graph.addNode(Node('t'))
graph.addEdge('s', 't', 1)

# adjacency matrix works but will get rediculously big
                 #   s,1,2,3,4,5,6,a,b,c,d,e,f,t
adjacency_matrix = [[0,1,1,1,1,1,1,0,0,0,0,0,0,0],# s
                    [0,0,0,0,0,0,0,0,1,1,0,0,0,0],# 1
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],# 2 
                    [0,0,0,0,0,0,0,1,0,0,1,0,0,0],# 3 
                    [0,0,0,0,0,0,0,0,0,1,0,0,0,0],# 4 
                    [0,0,0,0,0,0,0,0,0,1,1,0,0,0],# 5 
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,0],# 6 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,1],# a 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,1],# b 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,1],# c 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,1],# d 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,1],# e 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,1],# f 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,1]]# t 

# adjacency_list is ok, but it's missing the edge values
adjacency_list = {
    's': ['1', '2', '3', '4', '5', '6'],
    '1': ['b', 'c'],
    '2': [],
    '3': ['a', 'd'],
    '4': ['c'],
    '5': ['c', 'd'],
    '6': ['f'],
    'a': ['t'],
    'b': ['t'],
    'c': ['t'],
    'd': ['t'],
    'e': ['t'],
    'f': ['t']
}

# graph_table is like adjacency_matrix but more space efficient
X = ['1','2','3','4','5','6']
Y = ['a','b','c','d','e','f']
source = 's'
sink = 't'
nodes = ['s'] + X + Y + ['t']
graph_table = {}
for node in nodes:
    graph_table[node] = {}
for x in X:
    graph_table[source][x] = 1
graph_table['1']['b'] = 1
graph_table['1']['c'] = 1
graph_table['3']['a'] = 1
graph_table['3']['d'] = 1
graph_table['4']['c'] = 1
graph_table['5']['c'] = 1
graph_table['5']['d'] = 1
graph_table['6']['f'] = 1
for y in Y:
    graph_table[y][sink] = 1

def ford_fulkerson(G, source, sink):
    def dfs(u, target, history):
        if u == target:
            return history
        for v, edge in G[u].items():
            if edge > 0:
                result = dfs(v, target, history + [(u, v)])
                if result != None:
                    return result

    f_total = 0
    path = dfs(source, sink, [])
    while path is not None:
        print(path)
        f = inf
        for edge in path:
            u = edge[0]
            v = edge[1]
            f = min(f, G[u][v])
        f_total += f
        for edge in path:
            u = edge[0]
            v = edge[1]
            G[u][v] -= f
        path = dfs(source, sink, [])
    print("G:")
    for node, neighbours in G.items():
        print(node, neighbours)
    return 0

if __name__ == "__main__":
    main()

#    def bfs():
#        nonlocal parent
#        visited = [False]*V
#        queue = []
#        visited[source] = True
#        queue.append(source)
#        while queue:
#            u = queue.pop(0)
#            for i, v in enumerate(G[u]):
#                if visited[i] == False and v > 0:
#                    queue.append(i)
#                    visited[i] = True
#                    parent[i] = u
#        return visited[sink]

#    V = len(G)
#    F = [] # flow
#    for u in G:
#        F.append([0]*V)
#    parent = [-1]*V
#    max_flow = 0
#    source = 0
#    sink = 5
#    # augment flow while there is path from source to sink
#    bfs_count = 0
#    while bfs():
#        bfs_count += 1
#        print(bfs_count)
#        print(G)
#        path_flow = inf
#        s = sink
#        while(s != source):
#            path_flow = min(path_flow, G[parent[s]][s])
#            s = parent[s]
#        max_flow += path_flow
#        v = sink
#        while(v != source):
#            u = parent[v]
#            G[u][v] -= path_flow
#            G[u][v] += path_flow
#            v = parent[v]
#    return max_flow

