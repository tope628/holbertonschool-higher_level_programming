#!/usr/bin/python3
""" Add Attr Model
"""


def add_attribute(self, key, value):
    """ Adds attribute to dict """
    self.key = key
    self.value = value
        
    try:
        if self.key not in self.__dict__:
            self.__dict__[self.key] = self.value
    except:
        raise TypeError("can't add new attribute")
