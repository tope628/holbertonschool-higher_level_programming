#!/usr/bin/python3
""" Write File Module
"""


def write_file(filename="", text=""):
    """
     Args:
         filename (file): The first parameter.
         text (string): The second parameter.

     Returns:
        string: prints to text file.
    """
    with open(filename, mode='w',  encoding='utf-8') as f:
        return f.write(text)
