#!/usr/bin/python3

def max_integer(my_list=[]):
    len_list = len(my_list)

    if len_list == 0:
        return None
    else:
        max_val = 0
        for i in range(len_list):
            if my_list[i] > max_val:
                max_val = my_list[i]
        return max_val
