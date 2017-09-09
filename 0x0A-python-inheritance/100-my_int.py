#!/usr/bin/python3
""" MyInt Model
"""


class MyInt(int):
    """ MyInt Class """
    def __eq__(self, int):
        """ Inverses result of == """
        return super().__ne__(int)

    def __ne__(self, int):
        """ Inverses result of != """
        return super().__eq__(int)
