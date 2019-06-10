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
