#!/usr/bin/python3

def element_at(my_list, idx):
    # check if idx is -ve or out of range
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > (length - 1):
        return None
    else:
        return my_list[idx]
