#!/usr/bin/python3
""" Rectangle Module
"""


from models.base import Base


class Rectangle(Base):

    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
     Args:
         my_obj (object): The first parameter.
         filename (file): The second parameter.

     Returns:
        string: JSON string
        """
        super().__init__(id)
#        if type(width) is not int:
#            raise TypeError("width must be an integer")
#        elif width <= 0:
#            raise ValueError("width must be > 0")
#       else:
        self.__width = width
#       if type(height) is not int:
#           raise TypeError("height must be an integer")
#       elif height <= 0:
#            raise ValueError("height must be > 0")
#       else:
        self.__height = height
#       if type(x) is not int:
#           raise TypeError("x must be an integer")
#       elif x < 0:
#           raise ValueError("x must be >= 0")
#       else:
        self.__x = x
#       if type(y) is not int:
#           raise TypeError("y must be an integer")
#       elif y < 0:
#           raise ValueError("y must be >= 0")
#       else:
        self.__y = y
#
#    @property
#    def width(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        return self.__width
#
#    @width.setter
#    def width(self, value):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        if type(value) is not int:
#            raise TypeError("width must be an integer")
#        elif value <= 0:
#            raise ValueError("width must be > 0")
#        else:
#            self.__width = value
#
#    @property
#    def height(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        return self.__height
#
#    @height.setter
#    def height(self, value):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        if type(value) is not int:
#            raise TypeError("height must be an integer")
#        elif value <= 0:
#            raise ValueError("height must be > 0")
#        else:
#            self.__height = value
#
#    @property
#    def x(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        return self.__x
#
#    @x.setter
#    def x(self, value):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        if type(value) is not int:
#            raise TypeError("x must be an integer")
#        if value < 0:
#            raise ValueError("x must be >= 0")
#        else:
#            self.__x = value
#
#    @property
#    def y(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        return self.__y
#
#    @y.setter
#    def y(self, value):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        if type(value) is not int:
#            raise TypeError("y must be an integer")
#        if value < 0:
#            raise ValueError("y must be >= 0")
#        else:
#            self.__y = value
#
#    def area(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        return self.__width * self.__height
#
#    def display(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        for i in range(self.__y):
#            print()
#        for i in range(self.__height):
#            for x in range(self.__x):
#                print(' ', end='')
#            for x in range(self.__width):
#                print('#', end='')
#            print()
#
#    def __str__(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
#            self.id, self.__x, self.__y, self.__width, self.__height))
#
#    def update(self, *args, **kwargs):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        if args is not None:
#            for k, v in kwargs.items():
#                if k == "id":
#                    self.id = v
#                if k == "width":
#                    self.width = v
#                if k == "height":
#                    self.height = v
#                if k == "x":
#                    self.x = v
#                if k == "y":
#                    self.y = v
#
#    def to_dictionary(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        my_dict = {}
#        my_dict["id"] = self.id
#        my_dict["width"] = self.width
#        my_dict["height"] = self.height
#        my_dict["x"] = self.x
#        my_dict["y"] = self.y
#        return my_dict
