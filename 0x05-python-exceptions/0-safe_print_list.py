#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new_list = []
    try: 
        for i in range(x):
            print(my_list[x], end="")
            new_list.append(my_list[x])
        return new_list
    except IndexError:
            print(my_list[x], end="")
            return my_list[x]


