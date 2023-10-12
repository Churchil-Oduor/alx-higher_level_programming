#!/usr/bin/python3
'''Returns the JSON representation of an object(string)
'''
import json


def to_json_string(my_obj):

    '''
    Args:
        my_obj: object to be serialized.

    Returns:
        JSON representation of an object.

    '''
    res = json.dumps(my_obj)
    return res
