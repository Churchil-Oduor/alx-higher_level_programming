#!/usr/bin/python3

'''Defines a rectangle
'''


class Rectangle:
    """Initializing the square

    Args:
        width(int): width of rectangle
        height(int): height of rectangle

    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Returns width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of rectangle

        Args:
            value(int): value to be set as width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        Gets the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of rectangle.

        Args:
            value(int): value to be set as height.

        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >=0')
        else:
            self.__height = value

    def area(self):
        """
        Gets the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates Perimeter
        """
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns a rectangle
        """
        if (self.height * self.width) > 0:
            return '\n'.join('#' * self.width for i in range(self.height))
        return ''

    def __repr__(self):
        """
        Returns a repr represention that can be used to model the triangle
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """Prints the text below when the object is
        being deleted
        """
        print('{}'.format('Bye rectangle...'))
