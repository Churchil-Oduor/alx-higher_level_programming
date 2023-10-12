#!/usr/bin/python3
'''load_from_json_file
creates an Object from a “JSON file”.
'''
import json


def load_from_json_file(filename):
    '''
    Args:
        filename: JSON file containing contents to be
        made into objects.

    '''

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    obj = json.loads(text)
    return obj
