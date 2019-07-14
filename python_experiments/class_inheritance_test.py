#!/usr/bin/env python2.7


class A(object):
    def f(self):
        self.g()

    def g(self):
        print("g called from A")


class B(A):
    def g(self):
        print("g called from B")


b = B()
b.f()
