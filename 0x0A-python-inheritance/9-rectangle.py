#!/usr/bin/python3
"""Rectangle  Module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
"""Rectangle class"""
    def __init__(self, width, height):
    """
     Args:
         self (object): The first parameter.
         width (integer): The second parameter.
         height (integer): The third parameter.
    """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
 """
     Args:
         self (object): The first parameter.
"""
        return self.__width * self.__height

    def __str__(self):
    """
     Args:
         self (object): The first parameter.
    """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
