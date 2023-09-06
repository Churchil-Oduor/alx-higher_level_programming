#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upper = chr(ord(str[i]) - 97 + 65)
            print(upper, end="" if i < len(str) - 1 else "\n")
        else:
            print(str[i], end="" if i < len(str) - 1 else "\n")
