#!/usr/bin/python3
""" Line Number  Module
"""


def number_of_lines(filename=""):
    """
     Args:
         filename (file): The first parameter.

     Returns:
        int: number of lines in text file
    """
    with open(filename, encoding='utf-8') as f:
        linenum = 0
        for lines in f:
            linenum += 1
        return linenum
