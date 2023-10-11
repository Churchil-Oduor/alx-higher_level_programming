#!/usr/bin/python3
import json

'''Returns the JSON representation of an object(string)
'''


def to_json_string(my_obj):

    '''
    Args:
        my_obj: object to be serialized.

    Returns:
        JSON representation of an object.

    '''
    res = json.dumps(my_obj)
    return res
