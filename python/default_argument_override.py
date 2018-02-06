#!/usr/bin/env python3

def f(a, b=bytearray()):
    b.append(ord("i"))
    print(a+" r"+b.decode()+"ck !!!")

f("pickle")
f("pickle")
f("pickle")
f("pickle")
f("pickle")
f("pickle")
