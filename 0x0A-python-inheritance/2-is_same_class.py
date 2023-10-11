#!/usr/bin/python3

'''is_name_class checks if an object is an instance of the
specified class.
'''


def is_same_class(obj, a_class):
    '''
    Args:
        obj: first instance.
        a_class: second instance.

    Returns:
        returns True if the object is exactly an instance of the specified
        class. Otherwise false.
    '''
    return isinstance(obj, a_class)
