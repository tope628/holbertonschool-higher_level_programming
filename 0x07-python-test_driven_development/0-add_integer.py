"""Add Integer Module

This module takes 2 integers and/ or floats, and adds them.
otherwise raise a TypeError exception with the message a must be an
integer or b must be an integer. Floats must be casted into integers.

"""


def add_integer(a, b):
    """
     Args:
         a (int): The first parameter.
         b (int): The second parameter.

     Returns:
         int: Addition of a and b. TypeError otherwise.
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
