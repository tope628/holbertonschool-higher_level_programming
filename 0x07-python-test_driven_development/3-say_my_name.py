#!/usr/bin/python3
"""Say My Name Module

This module takes 2 strings and prints them. Otherwise raise a
TypeError exception with a message.

"""


def say_my_name(first_name, last_name=""):
    """
    Args:
         first_name (string): The first parameter.
         last_name (string): The second parameter.

    Returns:
         string: "My name is 'first_name' 'last_name'.
         TypeError otherwise.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
