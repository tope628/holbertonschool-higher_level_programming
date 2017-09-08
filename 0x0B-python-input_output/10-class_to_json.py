#!/usr/bin/python3
""" JSON Module
"""


def class_to_json(obj):
    """
     Args:
         obj (object): The first parameter.

     Returns:
        string: dictionary description
    """
    return obj.__dict__
