#!/usr/bin/env python3

import sys

def main():
    clusters = list()

    for line in sys.stdin:
        line = list(map(lambda x: x.rstrip(','), line.strip().split(' ')))

        if all([line[0] not in cluster for cluster in clusters]):
            clusters.append(set([line[0]]+line[2:]))
            continue

        merged_cluster = set()
        clusters_to_remove = []
        for cluster in clusters:
            if line[0] in cluster:
                for elem in cluster:
                    merged_cluster.add(elem)
                for elem in line[2:]:
                    merged_cluster.add(elem)
                clusters_to_remove.append(cluster)
        clusters.append(merged_cluster)

        for cluster in clusters_to_remove:
            clusters.remove(cluster)

    print(len(clusters))

if __name__ == "__main__":
    main()
