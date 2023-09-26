#!/usr/bin/python3

"""
class square defines a square with private attribute :size
"""
class Square:
    """The size attribute is private.

    Args:
        size: the size of the square.

    """
    def __init__(self, size):
        self.__size = size
