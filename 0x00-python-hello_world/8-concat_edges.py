#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

print(str[str.index('b') - 1 : str.index('l') - 1] + str[str.index('wi') - 1: str.index('wi') + 5] + str[0: str.index(' ')])
