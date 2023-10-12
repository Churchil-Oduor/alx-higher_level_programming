#!/usr/bin/python3
'''writes an Object to a text file, using a JSON representation.
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Args:
        my_obj: object to be written onto text file.
        filename: name of text file.
    '''
    text = json.dumps(my_obj)
    with open(filename, 'a', encoding='utf-8') as f:
        chars = f.write(text)
    return chars
