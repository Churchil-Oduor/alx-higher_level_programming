#!/usr/bin/python3


'''BaseGeometry class.
'''


class BaseGeometry:
    def __init__(self):
        pass
    '''area() raises an exception with
    the message area() is not implemented.

    '''

    def area(self):
        raise Exception('area() is not implemeted')

    '''integer_validator validates value.
    Args:
        name(str): always a string value.
        value(int): should be an int.

    '''

    def integer_validator(self, name, value):
        if value is int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater then zero'.format(name))


'''inherits from BaseGeometry
'''


class Rectangle(BaseGeometry):
    '''
    Args:
        width(int): width of rectangle.
        height(int): height of rectangle.
    '''

    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        self.integer_validator(type(self).__name__, height)
        self.integer_validator(type(self).__name__, width)
