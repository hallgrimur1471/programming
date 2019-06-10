#!/usr/bin/env python3.5
# pylint: disable=invalid-name,unused-argument,unused-variable
import sys
import random


def main():
    t = 10
    print(t)
    for case_num in range(1, t + 1):
        n = 200000000
        L = random.randint(25, 100)
        print("{} {}".format(n, L))

        primes = random_26_primes()
        primes = list(primes)
        primes.sort()

        plain = list(range(0, 26))
        while len(plain) < L + 1:
            plain.append(random.randint(0, 25))
        random.shuffle(plain)
        plain = list(map(lambda x: chr(x + ord("A")), plain))

        alphabet = "".join([chr(x + ord("A")) for x in range(0, 26)])
        primes.sort()
        cipher = []
        for i in range(0, len(plain) - 1):
            x = primes[alphabet.index(plain[i])]
            y = primes[alphabet.index(plain[i + 1])]
            cipher.append(x * y)

        cipher = " ".join(map(str, cipher))
        plain = "".join(plain)
        print(cipher)
        print("Case #{}: {}".format(case_num, plain), file=sys.stderr)


def random_26_primes():
    num_lines = 0
    with open("primes.txt", "r") as f:
        while f.readline():
            num_lines += 1

    primes = set()
    r = random.sample(range(0, num_lines), 26)
    r.sort(reverse=True)
    i = 0
    with open("primes.txt", "r") as f:
        while r:
            line_num = r.pop()
            while i < line_num:
                line = f.readline()
                i += 1
            line = line.split("\t")
            num_primes_in_line = len(line)
            rand_i = random.randint(0, num_primes_in_line - 1)
            prime = int(line[rand_i])
            primes.add(prime)
    return primes


def prnt(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    print(*args, **kwargs)


def dbg(*args, **kwargs):
    if "flush" not in kwargs:
        kwargs["flush"] = True
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    print(*args, **kwargs)


if __name__ == "__main__":
    main()
