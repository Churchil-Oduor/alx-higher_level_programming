#!/usr/bin/python3
import sys
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'
my_list = []
args = sys.argv[1:]
for arg in args:
    my_list.append(arg)

try:

    obj = load_from_json_file(filename)
    for item in my_list:
        obj.append(item)
    save_to_json_file(obj, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
