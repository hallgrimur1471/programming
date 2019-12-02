#!/usr/bin/env python3.7

import sys

def main():
    modules = []
    for line in sys.stdin:
        module = int(line.rstrip())
        modules.append(module)

    fuel_requirements = 0
    for module in modules:
        fuel_requirements += (module // 3) - 2
    
    print(f"Fuel requirements: {fuel_requirements}")

if __name__ == "__main__":
    main()
