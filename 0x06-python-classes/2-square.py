#!/usr/bin/python3

"""
class square defines a square.

"""
class Square:
    """class square defines a private instance attribute: size

    Args:
        size (int): size of the square in integer data type.

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size
