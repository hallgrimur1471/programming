#!/usr/bin/env python3

import sys
import time
from day_10_2_knot_hash import knot_hash

def main():
    start_time = time.time()

    inpt = sys.stdin.read().strip()

    disk = []
    for i in range(0, 128):
        k_hash = knot_hash(inpt+"-"+str(i))
        bits = map(lambda c: bin(int(c, 16))[2:].zfill(4), k_hash)
        bits = ''.join(list(bits))
        disk.append(bits)

    regions = []
    for i in range(0, 128):
        for j in range(0, 128):

            # only handle aces
            if disk[i][j] == '0':
                continue

            left_region = []
            top_region = []
            for region in regions:
                if i > 0 and (i-1, j) in region:
                    region.add((i,j))
                    left_region = region
                if j > 0 and (i, j-1) in region:
                    region.add((i,j))
                    top_region = region

            if left_region == [] and top_region == []:
                regions.append({(i,j)}) # i,j is at a newly discovered region
            elif left_region == [] and top_region != []:
                pass
            elif left_region != [] and top_region == []:
                pass
            elif left_region == top_region:
                pass
            else:
                # merge regions
                merged_region = set()
                for elem in left_region:
                    merged_region.add(elem)
                for elem in top_region:
                    merged_region.add(elem)
                regions.remove(left_region)
                regions.remove(top_region)
                regions.append(merged_region)

    print(len(regions))

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
