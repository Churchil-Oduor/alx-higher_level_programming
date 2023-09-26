#!/usr/bin/python3

"""
class square defines a square
"""


class Square:
    """Initializing a square

    Args:
        size (int): size of square in integer form

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Getter function

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter Function

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates area of the square

        """
        data = self.__size
        return (data * data)

    def my_print(self):
        """Prints the square in stdout using #

        l: length
        """
        for y in range(self.__size):
            for x in range(self.__size):
                print('{}'.format('#'), end="")
            print()
