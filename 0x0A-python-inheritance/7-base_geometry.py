#!/usr/bin/python3


'''BaseGeometry class.
'''


class BaseGeometry:
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
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater then 0'.format(name))
