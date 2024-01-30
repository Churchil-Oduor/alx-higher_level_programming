#!/usr/bin/python3
"""This module contains a function that adds 2 integers.
   The purpose is to learn python unittests.
"""


def add_integer(a, b=98):

    """This function adds two integers together

    Args:
        a (int): first parameter
        b (int): second int parameter

    Returns:
        int: sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
