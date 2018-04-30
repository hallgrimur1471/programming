#!/usr/bin/env python3

def unique(list_of_lists):
    return [list(x) for x in set(tuple(x) for x in list_of_lists)]

def partitions(x, m):
    p = [[]]
    if m == 0:
        return [x]
    for i in range(0, len(x)):
        p += partitions(x[0:i] + [x[i]+1] + x[i+1:], m-1)
    return list(filter(None, p))

def partitions_non_recursive(x, m):
    stack = []
    stack.append( (x, m) )

    return_stack = [[]]

    while stack:
        x, m = stack.pop()

        if m == 0:
            return_stack += [x]
            continue;
        for i in range(0, len(x)):
            stack.append( (x[0:i] + [x[i]+1] + x[i+1:], m-1) )
    return list(filter(None, return_stack))

print("recursive:    ", unique(partitions([0,0], 4)))
print("non-recursive:", unique(partitions_non_recursive([0,0], 4)))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def factorial_non_recursive(n):
    stack = []
    stack.append(n)

    return_val = None

    while stack:
        n = stack.pop()

        if n == 0:
            return_val = 1
        if return_val is None:
            # we go deeper
            stack.append(n)
            stack.append(n-1)
            continue

        return_stack.append(n)
        stack.append(n-1)

    # finally we can do the backwards calculations
    return_val = 1
    for x in return_stack:
        return_stack.pop()
    return prod(return_stack)


import sys
sys.setrecursionlimit(10000000)

factorial(100000)
print("done")
