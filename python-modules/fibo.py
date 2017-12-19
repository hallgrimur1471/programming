#!/usr/bin/env python3

# Fibonacci numbers module

BOLTZMANN_CONSTANT = 8.6173303 * 10**-5

# write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

# return Fibonacci serios up to n
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__": # true when this script is not being imported
    import sys
    fib(int(sys.argv[1]))
