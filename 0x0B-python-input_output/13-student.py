#!/usr/bin/python3
""" Student Module
"""


class Student:
    """ Student Class"""

    def __init__(self, first_name, last_name, age):
        """
         Args:
             first_name (string): The first parameter.
             last_name (string): The second parameter.
             age (int): The third parameter.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
         Args:
             self (class): The first parameter.
             attrs (list): The second parameter.

         Returns:
            string: dictionary description
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for key in attrs:
            try:
                my_dict[key] = self.__dict__[key]
            except:
                pass
        return my_dict

    def reload_from_json(self, json):
        """
         Args:
             self (class): The first parameter.
             json (dict): The second parameter.

         Returns:
            string: dictionary description
        """
        for k, v in json.items():
            self.__dict__[k] = v
