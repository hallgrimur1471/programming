#!/usr/bin/env python3

import sys
import math

def main():
    lengths = list(map(int, sys.stdin.read().strip().split(',')))
    x = list(range(0,256))
    i = 0
    skip_size = 0

    for d in lengths:
        if i+d >= len(x):
            sublist = x[i:] + x[:d-(len(x)-i)]
        else:
            sublist = x[i:i+d]

        sublist.reverse()

        for j in range(0, len(sublist)):
            x[(i+j) % len(x)] = sublist[j]

        i = (i+d+skip_size) % len(x)
        skip_size += 1

    print(x[0]*x[1])

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
import math
import itertools
from copy import copy

def main():
    inpt = sys.stdin.read().strip()
    print(knot_hash(inpt))

def knot_hash(inpt):
    lengths = list(map(ord, inpt))
    suffix = [17, 31, 73, 47, 23]
    lengths += suffix
    x = list(range(0,256))
    i = 0
    skip_size = 0

    for _ in itertools.repeat(None, 64):
        for d in lengths:
            if i+d >= len(x):
                sublist = x[i:] + x[:d-(len(x)-i)]
            else:
                sublist = x[i:i+d]
    
            sublist.reverse()
    
            for j in range(0, len(sublist)):
                x[(i+j) % len(x)] = sublist[j]
    
            i = (i+d+skip_size) % len(x)
            skip_size += 1

    sparse_hash = copy(x)

    dense_hash = []
    for i in range(0,16):
        k = sparse_hash[16*i]
        for j in range(1,16):
            k = k ^ sparse_hash[16*i + j]
        dense_hash.append(k)

    dense_hash = ''.join(list(map(lambda num: "{0:0{1}x}".format(num, 2), dense_hash)))
    return dense_hash

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
import math
import itertools
from copy import copy

def main():
    inpt = sys.stdin.read().strip()
    print(knot_hash(inpt))

def knot_hash(inpt):
    lengths = list(map(ord, inpt))
    suffix = [17, 31, 73, 47, 23]
    lengths += suffix
    x = list(range(0,256))
    i = 0
    skip_size = 0

    for _ in itertools.repeat(None, 64):
        for d in lengths:
            if i+d >= len(x):
                sublist = x[i:] + x[:d-(len(x)-i)]
            else:
                sublist = x[i:i+d]
    
            sublist.reverse()
    
            for j in range(0, len(sublist)):
                x[(i+j) % len(x)] = sublist[j]
    
            i = (i+d+skip_size) % len(x)
            skip_size += 1

    sparse_hash = copy(x)

    dense_hash = []
    for i in range(0,16):
        k = sparse_hash[16*i]
        for j in range(1,16):
            k = k ^ sparse_hash[16*i + j]
        dense_hash.append(k)

    dense_hash = ''.join(list(map(lambda num: "{0:0{1}x}".format(num, 2),
            dense_hash)))
    return dense_hash

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys

def main():
    x, y, z = 0, 0, 0
    path = sys.stdin.read().strip().split(',')

    for step in path:
        if step == "n":
            y += 1
            z += 1
        elif step == "ne":
            x += 1
            z += 1
        elif step == "se":
            x += 1
            y -= 1
        elif step == "s":
            y -= 1
            z -= 1
        elif step == "sw":
            x -= 1
            z -= 1
        elif step == "nw":
            x -= 1
            y += 1

    print(max(x,y,z))
    
if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys

def main():
    x, y, z = 0, 0, 0
    mx = 0
    path = sys.stdin.read().strip().split(',')

    for step in path:
        if step == "n":
            y += 1
            z += 1
        elif step == "ne":
            x += 1
            z += 1
        elif step == "se":
            x += 1
            y -= 1
        elif step == "s":
            y -= 1
            z -= 1
        elif step == "sw":
            x -= 1
            z -= 1
        elif step == "nw":
            x -= 1
            y += 1
        mx = max(mx, max(x,y,z))

    print(mx)
    
if __name__ == "__main__":
    main()
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

    zero_cluster = list(filter(lambda c: '0' in c, clusters))[0]
    print(len(zero_cluster))

if __name__ == "__main__":
    main()
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
#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    # construct firewall
    firewall = dict()
    for line in sys.stdin:
        line = list(map(int, line.strip().split(": ")))
        field = line[0]
        laser_range = line[1]
        firewall[field] = laser_range

    # find delay to escape through
    delay = -1
    passes_all = False
    while not passes_all:
        delay += 1

        passes_all = True
        for field, laser_range in firewall.items():
            if does_not_pass(field, laser_range, delay):
                passes_all = False
                break

    print("did not get caught using delay: "+str(delay))
    print("runtime: "+seconds_to_hms(time.time()-start_time))

def does_not_pass(f, r, d):
    a = d+f # packets arrives to layer at this time
    return a % (2*r-2) == 0

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
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

    s = sum(map(lambda row: sum(map(int, row)), disk))
    print(s)

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
#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    matches = 0

    a = int(sys.stdin.readline().strip().split(' ')[-1])
    b = int(sys.stdin.readline().strip().split(' ')[-1])

    a_factor = 16807
    b_factor = 48271

    magic = 2147483647

    for i in range(0,40000000):
        a = gen(a, a_factor, magic)
        a_bits = bin(a)[2:].zfill(32)[-16:]
        b = gen(b, b_factor, magic)
        b_bits = bin(b)[2:].zfill(32)[-16:]
    
        if a_bits == b_bits:
            matches += 1

    print(matches)

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def gen(v, f, n):
    return (v*f) % n

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    matches = 0

    a = int(sys.stdin.readline().strip().split(' ')[-1])
    b = int(sys.stdin.readline().strip().split(' ')[-1])

    a_factor = 16807
    b_factor = 48271

    magic = 2147483647

    for i in range(0,5000000):
        while a % 4 != 0:
            a = gen(a, a_factor, magic)
        a_bits = bin(a)[2:].zfill(32)[-16:]
        while b % 8 != 0:
            b = gen(b, b_factor, magic)
        b_bits = bin(b)[2:].zfill(32)[-16:]
    
        if a_bits == b_bits:
            matches += 1

        a = gen(a, a_factor, magic)
        b = gen(b, b_factor, magic)

    print(matches)

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def gen(v, f, n):
    return (v*f) % n

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    p = list(map(chr, range(ord('a'), ord('p')+1)))
    instructions = sys.stdin.read().strip().split(',')

    for instruction in instructions:
        instr = instruction[0]
        if instr == 's':
            x = int(instruction[1:])
            p = p[len(p)-x:] + p[:len(p)-x]
        elif instr == 'x':
            a, b = list(map(int, instruction[1:].split('/')))
            p[a], p[b] = p[b], p[a]
        elif instr == 'p':
            a, b = instruction[1:].split('/')
            a_i = p.index(a)
            b_i = p.index(b)
            p[a_i], p[b_i] = p[b_i], p[a_i]

    print(''.join(p))

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
#!/usr/bin/env python3

import sys
import time
from copy import copy

def main():
    start_time = time.time()

    num_dances = 1000000000
    p = list(map(chr, range(ord('a'), ord('p')+1)))
    p1 = copy(p) # before first dance
    instructions = sys.stdin.read().strip().split(',')

    history = []
    dance_num = 0
    found_loop = False
    while dance_num < num_dances:
        history.append(copy(p))

        if dance_num % 100 == 0:
            print(dance_num, seconds_to_hms(time.time()-start_time),
                ''.join(p))

        for instruction in instructions:
            instr = instruction[0]
            if instr == 's':
                x = int(instruction[1:])
                p = p[len(p)-x:] + p[:len(p)-x]
            elif instr == 'x':
                a, b = list(map(int, instruction[1:].split('/')))
                p[a], p[b] = p[b], p[a]
            elif instr == 'p':
                a, b = instruction[1:].split('/')
                a_i = p.index(a)
                b_i = p.index(b)
                p[a_i], p[b_i] = p[b_i], p[a_i]

        dance_num += 1

        if p in history and found_loop == False:
            loop_size = dance_num
            print("found loop!: ", loop_size)
            found_loop = True
            while dance_num < num_dances:
                dance_num += loop_size 
            dance_num -= loop_size
            print("dance_num increased to: "+str(dance_num))

    print(''.join(p))

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
#!/usr/bin/env python3

import sys
import time
from copy import copy, deepcopy

def main():
    start_time = time.time()

    steps = int(sys.stdin.read().strip())
    vortex = [0]
    i = 0

    for val in range(1, 2018):
        i = (i + (steps % len(vortex))) % len(vortex)
        vortex.insert(i+1, val)
        i = (i+1) % len(vortex)

    print(vortex[(vortex.index(2017)+1) % len(vortex)])

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
#!/usr/bin/env python3

import sys
import time
from copy import copy, deepcopy

def main():
    start_time = time.time()

    steps = int(sys.stdin.read().strip())
    vortex = [0]
    i = 0

    for val in range(1, 50000000+1):
        vortex_length = val # this is faster
        if val < 10:
            print(vortex)
        if val % 1000000 == 0:
            print(val)
        i = (i + (steps % vortex_length)) % vortex_length
        if i == 0:
            print("inserting after 0: "+str(val))
        #vortex.insert(i+1, val) # inserting to a list is slow!
        i = (i+1) % (vortex_length+1)

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
#!/usr/bin/env python3

import sys
import time
from copy import copy, deepcopy

def main():
    start_time = time.time()

    instructions = []
    for line in sys.stdin:
        instruction = line.strip().split(' ')
        instructions.append(instruction)

    registers = dict()

    i = 0
    recovered_a_frequency = False
    last_played_frequency = None
    while not recovered_a_frequency:
        instr = instructions[i]
        op = instr[0]
        x = instr[1]

        if x not in registers:
            registers[x] = 0

        if op == "snd":
            last_played_frequency = registers[x]
        elif op == "set":
            y = val_of(instr[2], registers)
            registers[x] = y
        elif op == "add":
            y = val_of(instr[2], registers)
            registers[x] += y
        elif op == "mul":
            y = val_of(instr[2], registers)
            registers[x] *= y
        elif op == "mod":
            y = val_of(instr[2], registers)
            registers[x] %= y
        elif op == "rcv" and registers[x] != 0:
            recovered_a_frequency = True
            continue
        elif op == "jgz" and registers[x] > 0:
            y = val_of(instr[2], registers)
            i += y
            continue

        print(i, instr, "registers: ", end='')
        for register, value in registers.items():
            print(register+":"+str(value), end=' ')
        print()

        i += 1

    print(last_played_frequency)

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def val_of(v, r):
    if v.isdigit() or (v[0]=="-" and v[1:].isdigit()):
        return int(v)
    else:
        # it's a register
        return r[v]

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
import time
import re
from copy import copy, deepcopy

class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = dict()
        self._is_waiting_for_data = False
        self.is_terminated = False
        self.num_sent_packets = 0
        self._instruction_pointer = 0
        self._instruction_register =\
                self.instructions[self._instruction_pointer]
        self._pipe = None
        self._received_values = []
        self._jumped_on_last_instruction = False

    def step(self):
        self._execute_current_instruction()
        if not (self._jumped_on_last_instruction or self._is_waiting_for_data):
            self._move_to_next_instruction()

    def set_pipe_to(self, program):
        self._pipe = program

    def receive_through_input(self, value):
        self._received_values.insert(0, value)

    def value_of_register(self, register):
        if register not in self.registers:
            self._initialize_register(register)
        return self.registers[register]

    def set_register(self, register, value):
        self.registers[register] = value

    def is_waiting_for_data(self):
        return self._received_values == [] and self._is_waiting_for_data

    def _execute_current_instruction(self):
        instruction = self._instruction_register
        operation = instruction.operation
        first_argument = instruction.first_argument
        if instruction.len() == 3:
            second_argument = instruction.second_argument
            second_argument_value = self._evaluate(second_argument)
        if first_argument.isalpha() and first_argument not in self.registers:
            self._initialize_register(first_argument)
        if operation == "snd":
            self._send_to_pipe(self._evaluate(first_argument))
            self.num_sent_packets += 1
        elif operation == "rcv":
            if self._received_values:
                self.registers[first_argument] = self._received_values.pop()
            else:
                self._is_waiting_for_data = True
                return
        elif operation == "jgz":
            first_argument_value = self._evaluate(first_argument)
            if first_argument_value > 0:
                self._jump(second_argument_value)
                return
            else:
                pass
        elif operation == "set":
            self.registers[first_argument] = second_argument_value
        elif operation == "add":
            self.registers[first_argument] += second_argument_value
        elif operation == "mul":
            self.registers[first_argument] *= second_argument_value
        elif operation == "mod":
            self.registers[first_argument] %= second_argument_value
        self._jumped_on_last_instruction = False
        self._is_waiting_for_data = False

    def _move_to_next_instruction(self):
        self._jump(1)

    def _send_to_pipe(self, value):
        if self._pipe is None:
            error("pipe not set, can not send value")
        self._pipe.receive_through_input(value)

    def _jump(self, jump_size):
        self._instruction_pointer += jump_size
        if self._instruction_pointer_is_out_of_bounds():
            self.is_termianted = True
            return
        self._instruction_register =\
                self.instructions[self._instruction_pointer]
        self._jumped_on_last_instruction = True

    def _instruction_pointer_is_out_of_bounds(self):
        return (self._instruction_pointer < 0 or 
                self._instruction_pointer > len(self.instructions)-1)

    def _evaluate(self, expression):
        # expression must be a string
        if not isinstance(expression, str):
            error("_evaluate only supports strings")
        # expression is either a number_string or a single letter register
        if re.match(r"[-+]?\d+$", expression) is not None:
            # expression is a number string
            return int(expression)
        if len(expression) != 1:
            error("_evalute only supports single letter registers")
        # expression is a single letter register
        return self.registers[expression]

    def _initialize_register(self, register):
        self.registers[register] = 0

class Instruction:
    def __init__(self, operation, first_argument, second_argument=None):
        self.operation = operation
        self.first_argument = first_argument # register
        self.second_argument = second_argument # number or register

    def len(self):
        if self.second_argument == None:
            return 2
        else:
            return 3

    def print(self):
        return (str(self.operation)+" "+str(self.first_argument)
                +" "+str(self.second_argument))

def main():
    start_time = time.time()
    instructions = []
    for line in sys.stdin:
        elems = line.strip().split(' ')
        if len(elems) == 2:
            instruction = Instruction(elems[0], elems[1])
        elif len(elems) == 3:
            instruction = Instruction(elems[0], elems[1], elems[2])
        else:
            error("invalid instruction length")
        instructions.append(instruction)
    A = Program(instructions)
    B = Program(instructions)
    A.set_register('p', 0)
    B.set_register('p', 1)
    A.set_pipe_to(B)
    B.set_pipe_to(A)
    deadlock = False
    finished = False
    while not (deadlock or finished):
        while not (A.is_waiting_for_data() or A.is_terminated):
            A.step()
        while not (B.is_waiting_for_data() or B.is_terminated):
            B.step()
        if A.is_waiting_for_data() and B.is_waiting_for_data():
            print("deadlock")
            deadlock = True
        if A.is_terminated and B.is_terminated:
            print("finished")
            finished = True
    print("Program B sent "+str(B.num_sent_packets)+" packets.")

def print_debug_info(msg, A, B):
    print(msg+" | A:"+str(A.registers), str(A._received_values)
                  +", B:"+str(B.registers), str(B._received_values))

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import numpy as np
import sys
import math
import time

class Lens:
    def __init__(self, width, height):
        if width != height:
            error("width and height must be equal")
        if width % 2 != 1:
            error("width and height must be odd integers")
        self._width = width
        self._height = height
        self._array = np.zeros((width, height), dtype=np.int)
        self._mid = math.floor(width/2)

    def add(self, num):
        self._array[self._mid][self._mid] = num + self._neighbours()

    def move(self, direction):
        if direction == "left":
            self._insert_zeros_at_column(0)
            self._delete_column_at(self._width)
        if direction == "right":
            self._insert_zeros_at_column(self._width)
            self._delete_column_at(0)
        if direction == "up":
            self._insert_zeros_at_row(0)
            self._delete_row_at(self._height)
        if direction == "down":
            self._insert_zeros_at_row(self._height)
            self._delete_row_at(0)

    def get_cursor_value(self):
        return self._array[self._mid][self._mid]

    def _insert_zeros_at_column(self, row):
        self._array = np.insert(self._array, row, 0, axis=1)

    def _delete_column_at(self, row):
        self._array = np.delete(self._array, row, axis=1)

    def _insert_zeros_at_row(self, column):
        self._array = np.insert(self._array, column, 0, axis=0)

    def _delete_row_at(self, column):
        self._array = np.delete(self._array, column, axis=0)

    def _neighbours(self):
        a = self._array
        m = self._mid
        return (sum(a[m-1][m-1:m+2])
               +sum(a[m+1][m-1:m+2])
               +sum(a[m][[m-1, m+1]]))

def error(msg):
     sys.stderr.write(msg) 
     sys.exit(1)

def get_next_direction(pos):
    x = pos[0]
    y = pos[1]
    N = max(abs(x), abs(y))
    if x == N and y > -N and y < N:
        return ("up", (x, y+1))
    elif y == N and x > -N:
        return ("left", (x-1, y))
    elif x == -N and y > -N:
        return ("down", (x, y-1))
    else:
        return ("right", (x+1, y))

def main():
    lens = Lens(21, 21)
    lens.add(1)
    position = (0,0)
    print(lens._array)

    current_value = lens.get_cursor_value()
    while current_value < 312051:
        direction, position = get_next_direction(position)
        lens.move(direction)
        lens.add(0)
        current_value = lens.get_cursor_value()
        print(lens._array, position)
        time.sleep(0.2)

if __name__ == "__main__":
    main()


#!/usr/bin/env python3

import day_3_2_spiral_memory as spiral

lens = spiral.Lens(5,5)
lens.add(1)
print(lens._array)
lens.move("right")
lens.add(0)
print(lens._array)
lens.move("up")
lens.add(0)
print(lens._array)
lens.move("left")
lens.add(0)
print(lens._array)
lens.move("left")
lens.add(0)
print(lens._array)
lens.move("down")
lens.add(0)
print(lens._array)
#!/usr/bin/env python3

import sys

valid_count = 0
for line in sys.stdin:
    word_list = line.rstrip("\n\r").split(sep=" ")
    if len(word_list) == len(set(word_list)):
        valid_count += 1

print(valid_count)
#!/usr/bin/env python3

import sys

valid_count = 0
for line in sys.stdin:
    word_list = line.rstrip("\n\r").split(sep=" ")
    if len(word_list) == len(set(map(''.join, list(map(sorted, word_list))))):
        valid_count += 1

print(valid_count)
#!/usr/bin/env python3

import sys

maze = list(map(lambda x: int(str.strip(x)), sys.stdin))
i = 0
steps = 0
while i < len(maze) and i >= 0:
    if maze[i] >= 3:
        offset = -1
    else:
        offset = 1
    maze[i] += offset
    i += (maze[i]-offset)
    steps += 1
print(steps)
#!/usr/bin/env python3

from copy import copy

def main():
    with open('day-6-memory-reallocation.input', 'r') as f:
        data = f.read()
    memory_banks = list(map(int, data.rstrip().split('\t')))

    history = []
    allocations = 0
    while memory_banks not in history:
        print(memory_banks)
        history.append(copy(memory_banks))
        r = max(memory_banks)
        i = memory_banks.index(r)
        memory_banks[i] = 0
        
        while r > 0:
            i = (i+1) % len(memory_banks)
            memory_banks[i] += 1
            r -= 1

        allocations += 1

    print(allocations)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

from copy import copy

def main():
    with open('day-6-memory-reallocation.input', 'r') as f:
        data = f.read()
    memory_banks = list(map(int, data.rstrip().split('\t')))

    history = []
    allocations = 0
    while memory_banks not in history:
        print(memory_banks)
        history.append(copy(memory_banks))
        r = max(memory_banks)
        i = memory_banks.index(r)
        memory_banks[i] = 0
        
        while r > 0:
            i = (i+1) % len(memory_banks)
            memory_banks[i] += 1
            r -= 1

        allocations += 1

    print(allocations)
    print(allocations - history.index(memory_banks))

if __name__ == "__main__":
    main()
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
#!/usr/bin/env python3

import sys

def main():
    registers = dict()
    for line in sys.stdin:
        line = line.strip().split(' ')

        instr_reg = line[0]
        instr_op = line[1]
        instr_val = int(line[2])
        cond_reg = line[4]
        cond_op = line[5]
        cond_val = int(line[6])

        if instr_reg not in registers:
            registers[instr_reg] = 0
        if cond_reg not in registers:
            registers[cond_reg] = 0

        cond_is_true = check_cond(cond_reg, cond_op, cond_val, registers)
        
        if cond_is_true:
            run_instr(instr_reg, instr_op, instr_val, registers)

    for register, value in registers.items():
        print(register, value)

    print(max(registers.values()))

def check_cond(reg, op, val, registers):
    reg_val = registers[reg]

    if op == '>':
        return reg_val > val
    elif op == '>=':
        return reg_val >= val
    elif op == '==':
        return reg_val == val
    elif op == '!=':
        return reg_val != val
    elif op == '<=':
        return reg_val <= val
    elif op == '<':
        return reg_val < val

def run_instr(reg, op, val, registers):
    if op == 'inc':
        registers[reg] += val
    elif op == 'dec':
        registers[reg] -= val
    else:
        error("run_instr")

def error(msg):
    sys.stderr.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
import math

def main():
    registers = dict()
    highest = -math.inf
    for line in sys.stdin:
        line = line.strip().split(' ')

        instr_reg = line[0]
        instr_op = line[1]
        instr_val = int(line[2])
        cond_reg = line[4]
        cond_op = line[5]
        cond_val = int(line[6])

        if instr_reg not in registers:
            registers[instr_reg] = 0
        if cond_reg not in registers:
            registers[cond_reg] = 0

        cond_is_true = check_cond(cond_reg, cond_op, cond_val, registers)
        
        if cond_is_true:
            run_instr(instr_reg, instr_op, instr_val, registers)
            highest = max(highest, registers[instr_reg])

    print(highest)

def check_cond(reg, op, val, registers):
    reg_val = registers[reg]

    if op == '>':
        return reg_val > val
    elif op == '>=':
        return reg_val >= val
    elif op == '==':
        return reg_val == val
    elif op == '!=':
        return reg_val != val
    elif op == '<=':
        return reg_val <= val
    elif op == '<':
        return reg_val < val

def run_instr(reg, op, val, registers):
    if op == 'inc':
        registers[reg] += val
    elif op == 'dec':
        registers[reg] -= val
    else:
        error("run_instr")

def error(msg):
    sys.stderr.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys

def main():
    stream = sys.stdin
    in_junk = False
    score = 0
    level = 0
    
    reached_end = False
    while not reached_end:
        c = stream.read(1)
        if c == '\n':
            reached_end = True
        elif c == '{' and not in_junk:
            level += 1
            score += level
        elif c == '}' and not in_junk:
            level -= 1
        elif c == '!' and in_junk:
            stream.read(1)
        elif c == '<' and not in_junk:
            in_junk = True
        elif c == '>' and in_junk:
            in_junk = False
        else:
            pass

    print(score)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys

def main():
    stream = sys.stdin
    in_junk = False
    score = 0
    level = 0
    junk_chars = 0
    
    reached_end = False
    while not reached_end:
        c = stream.read(1)
        if c == '\n':
            reached_end = True
        elif c == '{' and not in_junk:
            level += 1
            score += level
        elif c == '}' and not in_junk:
            level -= 1
        elif c == '!' and in_junk:
            stream.read(1)
        elif c == '<' and not in_junk:
            in_junk = True
        elif c == '>' and in_junk:
            in_junk = False
        elif in_junk:
            junk_chars += 1
        else:
            pass

    print(score, junk_chars)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import requests
import sys
import argparse

def main():
    args = parse_args()
    inpt = get_input(args.DAY, args.COOKIE)
    sys.stdout.write(inpt)

def get_input(day, cookie):
    headers = {'session': cookie}
    url = 'https://adventofcode.com/2017/day/'+day+'/input'
    session = requests.Session()
    response = session.get(url, cookies=headers)
    return response.text

def parse_args():
    parser = argparse.ArgumentParser()
    parser.description = ("Fetches and prints input for AoC problem")
    parser.add_argument("DAY", help="a number from 1-25. Fetch input for DAY")
    parser.add_argument("COOKIE", help="session cookie for your log-in session "
            "on AoC, look it up in your brower")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
import time
from copy import copy, deepcopy

def main():
    start_time = time.time()

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
