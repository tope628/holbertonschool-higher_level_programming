#!/usr/bin/python3
""" Append File Module
"""


def append_write(filename="", text=""):
    """
     Args:
         filename (file): The first parameter.
         text (string): The second parameter.

     Returns:
        string: prints to text file.
    """
    with open(filename, mode='a',  encoding='utf-8') as f:
        return f.write(text)
