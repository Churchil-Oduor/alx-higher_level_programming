#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    len_list = len(my_list) - 1
    # checking if idx < 0 or out of range
    if idx < 0 or idx > len_list:
        return my_list
    else:

