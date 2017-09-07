#!/usr/bin/python3
"""Square Module
"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
"""square class"""
    def __init__(self, size):
    """
     Args:
         self (object): The first parameter.
         size (integer): The second parameter.
     """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
     """
     Args:
         self (object): The first parameter.
     """
        return self.__size ** 2

    def __str__(self):
    """
     Args:
         self (object): The first parameter.
     """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
