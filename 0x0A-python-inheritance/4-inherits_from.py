#!/usr/bin/python3

'''function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
'''


def inherits_from(obj, a_class):
    '''
    Args:
        obj: instance of a class.
        a_class: class

    Return:
        True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified
        class ; otherwise False.
    '''

    return (type(obj) is not a_class) and issubclass(type(obj), a_class)
