#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list) - 1
    while length != -1:
        element = my_list[length]
        print("{}".format(element))
        length -= 1
