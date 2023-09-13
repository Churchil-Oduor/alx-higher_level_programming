#!/usr/bin/python3

# adds all unique integers in a list

def uniq_add(my_list=[]):
    # creating a set
    my_set = set(my_list)
    summ = 0
    for i in my_set:
        summ += i
    return summ

