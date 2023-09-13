#!/usr/bin/python3

#  Returns a key with the biggest integer value.
def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    dict_len = len(a_dictionary)
    keys = list(a_dictionary)
    vals = [keys[x] for x in range(dict_len)]
    index = vals.index(max(vals))
    return keys[index]
