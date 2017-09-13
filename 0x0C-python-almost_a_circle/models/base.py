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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
     Args:
         list_dictionaries (dict): The first parameter.

     Returns:
        string: JSON string
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
     Args:
         cls (class): The first parameter.
         list_objs (list): The second parameter.

     Returns:
        string: JSON string
        """
        my_list = []
        filename = cls.__name__+".json"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write([])
            else:
                for obj in list_objs:
                    my_dict = obj.to_dictionary()
                    my_list.append(my_dict)
                json_list = cls.to_json_string(my_list)
                f.write(json_list)
