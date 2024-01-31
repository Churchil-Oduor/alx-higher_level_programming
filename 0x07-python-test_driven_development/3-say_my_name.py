#!/usr/bin/python3
"""This module contains a function that prints the
name of a person"""


def say_my_name(first_name, last_name=""):
    """This is the function that prints the name of a
    Person.

    Args:
        first_name (str): 1st name of a person.
        last_name (str): last name of a person.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    elif first_name == None and last_name == None:
        raise TypeError("say_my_name() missing 1 required positional argument: \'first_name\'")
    else:
        message = "My name is {} {}"
        print(message.format(first_name, last_name))
