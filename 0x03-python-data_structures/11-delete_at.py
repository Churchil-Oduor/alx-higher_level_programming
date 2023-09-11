#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    # check if idx is out of range and if idx is negative
    if idx < 0 or idx >= len(my_list):
        return my_list

    len_list = len(my_list)

    while idx < len_list:
        if (idx + 1) == len_list:
            break
        else:
            my_list[idx] = my_list[idx + 1]
        idx += 1
    del my_list[len_list - 1]
    return my_list
