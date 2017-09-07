#!/usr/bin/python3
"""Inherits  Module
"""
def inherits_from(obj, a_class):
    """
     Args:
         obj (object): The first parameter.
         a_class (object): The second  parameter.

     Returns:
         bool: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
