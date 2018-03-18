#!/usr/bin/env python3

from time import time
from math import floor

N = 10**5

v = [True]*N

t1 = time()
any(v)
t2 = time()
print("any took: {} minutes {} seconds".format(floor((t2-t1)/60), (t2-t1) % 60))
