#!/usr/bin/python3

"""
Advanced square
"""


class Square:
    """Initializing the square

    Args:
        size (int): size of the square in integer format.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def size(self):
        """Retrieve the data

        """
        data = self.__size
        return data

    def size(self, value):
        """setter function

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates area of the square
        """
        data = self.__size
        return (data * data)
