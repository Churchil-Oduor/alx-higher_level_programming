#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # create a copy of list

    copy = []
    length = len(my_list)
    index = 0
    while index != length:
        copy.append(my_list[index])
        index += 1

    if idx < 0:
        return my_list
    elif (length - 1) < idx:
        return my_list
    else:
        copy[idx] = element
        return copy
