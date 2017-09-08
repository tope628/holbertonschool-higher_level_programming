#!/usr/bin/python3
""" JSON Module
"""


class Student:
    """ student class"""

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

    def to_json(self):
        """
         Args:
             self (class): The first parameter.

         Returns:
            string: dictionary description
        """
        return self.__dict__
