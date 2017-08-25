"""Print Square Module

This module prints a square with a hashtag. Otherwise raise a TypeErr
or or ValueError exception. Floats must be casted into integers.

"""


def print_square(size):
    """
     Args:
         size (int): Length of square.

     Returns:
         string: Square as hashtags. TypeError/ ValueError otherwise.
    """
    if type(size) == float:
        size = int(size)
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        print('#' * size)
