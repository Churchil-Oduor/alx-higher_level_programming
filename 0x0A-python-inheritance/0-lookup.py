#!/usr/bin/python3


'''This module contains only the lookup function.
'''


def lookup(obj):
    '''
    Args:
        obj: is an object having attributes
        that are looked up by the function lookup.

    Returns:
        a list containing method and attribute names.
    '''
    return (dir(obj))
