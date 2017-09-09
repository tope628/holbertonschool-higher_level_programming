#!/usr/bin/python3
""" MyInt Model
"""

class MyInt(int):
    """ MyInt Class """
    def __eq__(self, int):
        """ Inverses result of == """
        self.int = int
        return not self.int	
    def __ne__(self, int):
        """ Inverses result of != """
        self.int = int
        return not self.__eq__(self.int)
