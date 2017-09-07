#!/usr/bin/python3
"""Lookup  Module
"""


def lookup(obj):
    """
     Args:
         obj (object): The first parameter.

     Returns:
         list: list of available attributes and methods of an object.
    """
    my_list = dir(obj)
    return my_list
