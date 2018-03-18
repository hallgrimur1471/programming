#!/usr/bin/env python3

from random import randint
from time import time

def my_any():
    pass

def main():
    N = 10**5

    # construct s, t lists of N random integers
    t = [0]*N
    s = [0]*N
    for i in range(N):
        t[i] = randint(0, 100*N)
    for i in range(N):
        s[i] = randint(0, 100*N)

    # we want to check if there exists an element sp in s that is also in t

    # checking using any()
    t1 = time()
    any([(se in t) for se in s])
    t2 = time()
    print("any took: {} minutes {} seconds".format(floor((t2-t1)/60), (t2-t1) % 60))

    # checking using my_any()
    t1 = time()
    my_any(s, t)
    t2 = time()
    print("my_any took: {} seconds".format(t2-t1))

if __name__ == "__main__":
    main()
