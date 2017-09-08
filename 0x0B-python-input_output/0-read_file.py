#!/usr/bin/python3
""" Read File Module
"""


def read_file(filename=""):
    """
     Args:
         filename (file): The first parameter.

     Returns:
        string: prints to stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
