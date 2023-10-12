#!/usr/bin/python3
'''function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
'''
import json


def class_to_json(obj):
    '''
    Args:
        obj: instance of an object.

    Returns:
        dictionary description with
        simple data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object.

    '''
    text = json.dumps(obj.__dict__)
    return text
