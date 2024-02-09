#!/usr/bin/python3

'''is_kind_of_class checks if an object is an instance of a class
that inherited from the specified class. otherwise False.
'''


def is_kind_of_class(obj, a_class):
    '''
    Args:
        obj: instance to be compared if instance of  a_class.
        a_class: a class

    Returns:
        True if the object is an instance of or is the object is an instance
        of a class that inherited from the specified class.

    '''

    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
