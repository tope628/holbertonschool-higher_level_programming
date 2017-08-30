#!/usr/bin/python3
"""Matrix Divided Module

This module divides all elements of a matrix. Otherwise raise a
TypeError exception or ZeroDivisionError exception
with custom error messages.

"""


def matrix_divided(matrix, div):
    """
     Args:
         matrix (list): The first parameter.
         div (int): The second parameter.

     Returns:
         list: All elements of matrix divided by div and original
	 matrix the same.
    """
    new_list = []
    if type(matrix) != list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(div) != int and type(div) != float:
         raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    equal_len = len(matrix[0])
    for x in matrix:
        if type(x) != list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        if len(x) != equal_len:
            raise TypeError("Each row of the matrix must have the\
 same size")
        for i in x:
            if type(i) == int or type(i) == float:
                new_list.append(round((i / div), 2))
            else:
                raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")
    return new_list
