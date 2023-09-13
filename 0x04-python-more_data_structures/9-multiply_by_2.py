#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    keys = list(a_dictionary)

    return {keys[i]: a_dictionary[keys[i]] * 2 for i in range(len(keys))}
