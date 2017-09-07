#!/usr/bin/python3
"""BaseGeometry  Module
"""
class BaseGeometry:
	""" base geometry class """
    def area(self):
    """
     Args:
         self (object): The first parameter.

    """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
  """
     Args:
         self (object): The first parameter.
         name (string): The second parameter.
         value (integer): The third parameter.

    """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
            
