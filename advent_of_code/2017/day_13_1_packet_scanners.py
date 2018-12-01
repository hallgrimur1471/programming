#!/usr/bin/env python3

import sys

class Layer:
    def __init__(self, rnge):
        self.range = rnge
        self.pos = 0
        self.dir = "down"

    def step(self):
        if self.pos == self.range-1 and self.dir == "down":
            self.dir = "up"
        elif self.pos == 0 and self.dir == "up":
            self.dir = "down"

        if self.dir == "down":
            self.pos += 1
        elif self.dir == "up":
            self.pos -= 1
        else:
            error("step")

def main():
    firewall = dict()
    severity = 0
    for line in sys.stdin:
        line = list(map(int, line.strip().split(": ")))
        p = line[0]
        r = line[1]

        firewall[p] = Layer(r)

    packet_pos = -1
    goal = max(firewall.keys())

    while packet_pos < goal:
        # update packet
        packet_pos += 1
        if packet_pos in firewall: # there is layer here
            layer = firewall[packet_pos]
            if layer.pos == 0:
                print("Caught at "+str(packet_pos)"! "
                        + "layer range: "+str(layer.range))
                severity += packet_pos * layer.range
    
        # update layers
        for pos in firewall:
            layer = firewall[pos]
            layer.step()

    print(severity)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
