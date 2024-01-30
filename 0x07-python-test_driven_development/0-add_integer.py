#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) or type(b) not int:
        raise TypeError("a must be an integer or b must be an integer")

    return a + b
