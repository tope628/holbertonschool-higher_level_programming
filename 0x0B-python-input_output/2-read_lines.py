#!/usr_bin/python3
""" Line Number  Module
"""


number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """
     Args:
         filename (file): The first parameter.
         nb_lines (int): The first parameter.

     Returns:
        string: prints lines in text file
    """
    with open(filename, encoding='utf-8') as f:
        linenum = number_of_lines(filename)
        if nb_lines <= 0 or nb_lines >= linenum:
            print(f.read(), end='')
        else:
            for x, lines in enumerate(f):
                if x == nb_lines:
                    break
                print(lines, end='')
