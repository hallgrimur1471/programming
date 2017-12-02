#!/usr/bin/env python3

# import fibo: Python looks for fibo.py in every directory of sys.path
# sys.path is initialised with these locations:
#     Current directory
#     PYTHONPATH
#     installation-dependent default
import fibo

print(dir(fibo))
fibo.fib(1000)
x = fibo.fib2(400)
print(x)
