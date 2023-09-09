#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 >= 2 and len2 >= 2:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return (new_tuple)

    elif len1 < 2 or len2 < 2:
        if len1 < 2 and len2 >= 2:
            if len1 == 1:
                new_tuple = (tuple_a[0] + tuple_b[0], tuple_b[1])
                return (new_tuple)
            new_tuple = (tuple_b[0], tuple_b[1])
            return (new_tuple)

        elif len2 < 2 and len1 >= 2:
            if len2 == 1:
                new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1])
                return (new_tuple)
            new_tuple = (tuple_a[0], tuple_b[0])
            return (new_tuple)

        else:
            new_tuple = (0, 0)
            return (new_tuple)
