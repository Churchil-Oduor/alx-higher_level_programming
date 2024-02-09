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
        self.width = width
        self.height = height

    '''
    String function
    '''
    def __str__(self):
        width = self.width
        height = self.height
        class_name = self.__class__.__name__
        message = '[{}] {}/{}'.format(class_name, width, height)
        return (message)

    '''
    computes area
    '''
    def area(self):
        return (self.width * self.height)


'''Square class
'''


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator('Square', size)
        self.__size = size

    def area(self):
        return self.__size ** 2
