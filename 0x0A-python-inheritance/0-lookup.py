#!/usr/bin/python3

def lookup(obj):
    '''
    Args:
        obj: is an object having attributes
        that are looked up by the function lookup.

    '''
    return (list(obj.__dict__))
