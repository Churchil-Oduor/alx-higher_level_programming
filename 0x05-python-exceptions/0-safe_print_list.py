#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for y in range(x):
            print(my_list[y], end="")
            count = 1 + count
        print()
        return count
    except IndexError:
        print()
        return count
