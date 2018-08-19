#!/usr/bin/env python3

from math import inf

def main():
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
    source = 0
    sink = 13
    mx, F = ford_fulkerson(adjacency_matrix, source, sink)
    print("max flow:", mx)
    print("F:")
    for line in F:
        print(line)

def ford_fulkerson(G, source, sink):
    def find_augmenting_path(u, target, history):
        candidates = []
        for v, value in enumerate(G[u]):
            if G[u][v] - F[u][v] > 0:
                candidates.append(v)
        if candidates == None:
            return None
        for v in candidates:
            if v == target:
                return history + [(u, v)]
            if (u,v) not in history:
                path = find_augmenting_path(v, target, history + [(u, v)])
                if path == None:
                    pass # we should try more
                else:
                    return path
        return None # no neighbours gave us a path to target
    F = []
    for line in G:
        F.append([0]*len(G))
    path = find_augmenting_path(source, sink, [])
    while path is not None:
        flow = inf
        for edge in path:
            u = edge[0]
            v = edge[1]
            flow = min(flow, G[u][v] - F[u][v])
        for edge in path:
            u = edge[0]
            v = edge[1]
            F[u][v] += flow
            F[v][u] -= flow
        path = find_augmenting_path(source, sink, [])
    maximum_flow = sum([x for x in F[source]])
    return maximum_flow, F

if __name__ == "__main__":
    main()
