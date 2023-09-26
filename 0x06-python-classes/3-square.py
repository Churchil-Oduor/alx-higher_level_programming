#!/usr/bin/python3

"""
class square defines a square

"""


class Square:
    """Initializing the class square and doing checks on input

    Args:
        size (int): integer to be fed into the square.

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        length is the length of the square.
        """
        length = self.__size
        return (length * length)
