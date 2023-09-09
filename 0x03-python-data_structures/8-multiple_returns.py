#!/usr/bin/python3

def multiple_returns(sentence):
    len_str = len(sentence)
    if len_str > 0:
        tup = (len_str, sentence[0])
        return tup
    else:
        tup = (len_str, None)
        return tup
