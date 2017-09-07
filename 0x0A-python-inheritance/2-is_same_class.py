#!/usr/bin/python3
"""Same Class  Module
"""


def is_same_class(obj, a_class):
    """
     Args:
         obj (object): The first parameter.
         a_class (object): The second  parameter.

     Returns:
         bool: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
