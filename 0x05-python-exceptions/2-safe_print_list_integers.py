#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            val = my_list[i]
            if type(val) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count
    except IndexError:
        raise IndexError from None
