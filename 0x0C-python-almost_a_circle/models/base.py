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
                f.write(cls.to_json_string(my_list))
            else:
                for obj in list_objs:
                    my_dict = obj.to_dictionary()
                    my_list.append(my_dict)
                f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
     Args:
         json_string (dict): The first parameter.

     Returns:
        list: JSON list of instances
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
     Args:
         cls (class): The first parameter.
         dictionary (dict): The second parameter.

     Returns:
        dummy (object): instance with set attributes.
        """
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            dummy = Rectangle(1, 1)
        if cls.__name__ == "Square":
            from models.square import Square
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
     Args:
        cls (class): The first parameter.
     Returns:
        list (list): instance with set attributes.
        """

        filename = cls.__name__+".json"
        if filename == None:
            return []
        with open(filename, mode='r', encoding='utf-8') as f:
            my_json = cls.from_json_string(f.read())
        for inst in my_json:
                return [cls.create(**inst)]
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
     Args:
         cls (class): The first parameter.
         list_objs (list): The second parameter.

     Returns:
        string: JSON string
        """
        my_list = []
        filename = cls.__name__+".csv"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write(cls.to_json_string(my_list))
            else:
                for obj in list_objs:
                    my_dict = obj.to_dictionary()
                    my_list.append(my_dict)
                f.write(cls.to_json_string(my_list))

    @classmethod
    def load_from_file_csv(cls):
        """
     Args:
        cls (class): The first parameter.
     Returns:
        list (list): instance with set attributes.
        """

        filename = cls.__name__+".csv"
        if filename == None:
            return []
        with open(filename, mode='r', encoding='utf-8') as f:
            my_json = cls.from_json_string(f.read())
        my_list = []
        for inst in my_json:
                my_list.append(cls.create(**inst))
        return my_list
