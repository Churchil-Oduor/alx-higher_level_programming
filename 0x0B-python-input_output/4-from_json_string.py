#!/usr/bin/python3
import json

'''a function that returns an object (Python data structure)
represented by a JSON string
'''


def from_json_string(my_str):
    '''
    Args:
        my_str: string to be deserialized to an object.

    Returns:
        a json object.
    '''
    obj = json.loads(my_str)
    return obj
