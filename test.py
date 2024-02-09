#!/usr/bin/python3

class A(object):
    def __init__(self, n="Rahul"):
        self.name = n


class B(A):
    def __init__(self, n, roll):
        self.roll = roll
        A.__init__(self, n)

object = B("Churchil", "Prefect")
print(object.name)
