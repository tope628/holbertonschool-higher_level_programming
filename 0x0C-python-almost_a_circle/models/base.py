#!/usr/bin/python3
""" Base Module
"""
import json


class Base:

    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
    Args:
         id (int): The first parameter.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
     Args:
         list_dictionaries (dict): The first parameter.

     Returns:
        string: JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries =  []
        return json.dumps(list_dictionaries)
#
#    def save_to_file(cls, list_objs):
#        """
#     Args:
#         cls (class): The first parameter.
#         list_objs (list): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#    with open(filename, mode='w', encoding='utf-8') as f:
#        to_json_file(list)
#        json.dump(cls, f)
