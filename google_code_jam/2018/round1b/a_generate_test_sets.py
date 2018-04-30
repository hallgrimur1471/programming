#!/usr/bin/env python3

from random import randint

for test_set in range(1, 4):
    T = 100
    with open("test_set_a{}.in".format(test_set), 'w') as f:
        print(T, file=f)
        for _ in range(0, T):
            if test_set == 1:
                N = randint(2, 25)
            elif test_set == 2:
                N = randint(2, 250)
            elif test_set == 3:
                N = randint(2, 10**5)
            L = randint(1, N-1)
            C_total = randint(L, N-1)
            C = [0]*L
            while C_total > 0:
                i = randint(0, L-1)
                C[i] += 1
                C_total -= 1
            print(' '.join([str(N), str(L)]), file=f)
            print(' '.join(map(str, C)), file=f)
