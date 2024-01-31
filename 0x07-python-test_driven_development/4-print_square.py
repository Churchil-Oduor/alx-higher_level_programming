#!/usr/bin/python3

"""module containing function that prints a
square width dimensions equal to the parameter
passed"""


def print_square(size):
    """function that prints a square with the character #.

    Args:
        size (int): length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
