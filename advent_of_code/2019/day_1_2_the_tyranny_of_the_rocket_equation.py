#!/usr/bin/env python3.7

import sys

def main():
    modules = []
    for line in sys.stdin:
        module = int(line.rstrip())
        modules.append(module)

    sum_of_fuel_requirements = 0
    for module in modules:
        fuel_requirement = calculate_module_fuel_requirement(module)
        sum_of_fuel_requirements += fuel_requirement
    
    print(f"Fuel requirements: {sum_of_fuel_requirements}")

def calculate_module_fuel_requirement(module):
    fuel_sum = 0

    fuel_requirement = max(0, (module // 3) - 2)
    fuel_sum += fuel_requirement
    while fuel_requirement > 0:
        fuel_requirement = max(0, (fuel_requirement // 3) - 2)
        fuel_sum += fuel_requirement

    return fuel_sum


if __name__ == "__main__":
    main()
