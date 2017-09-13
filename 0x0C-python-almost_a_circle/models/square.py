#!/usr/bin/python3
""" Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """
     Args:
         my_obj (object): The first parameter.
         filename (file): The second parameter.

     Returns:
        string: JSON string
        """
        super().__init__(size, size, x, y, id)
        self.size = size
#
#    @property
#    def size(self):
#        """
#     Args:
#         my_obj (object): The first parameter.
#         filename (file): The second parameter.
#
#     Returns:
#        string: JSON string
#        """
#        return self.width
#
#    @size.setter
#    def size(self, value):
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
#            self.width = value
#            self.height = value

    def __str__(self):
        """
     Args:
         my_obj (object): The first parameter.
         filename (file): The second parameter.

     Returns:
        string: JSON string
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))
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
#        if len(args) == 0:
#            for k, v in kwargs.items():
#                if k == "id":
#                    self.id = v
#                if k == "size":
#                    self.size = v
#                if k == "x":
#                    self.x = v
#                if k == "y":
#                    self.y = v
#        else:
#            for idx, arg in enumerate(args):
#                if idx == 0:
#                    self.id = arg
#                if idx == 1:
#                    self.size = arg
#                if idx == 2:
#                    self.x = arg
#                if idx == 3:
#                    self.y = arg
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
#        my_dict["size"] = self.size
#        my_dict["x"] = self.x
#        my_dict["y"] = self.y
#        return my_dict
