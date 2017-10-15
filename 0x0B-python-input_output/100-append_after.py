#!/usr/bin/python3
""" Append File Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
     Args:
         filename (file): The first parameter.
         search_string (string): The second parameter.
         new_string (string): The second parameter.

     Returns:
        string: prints to text file.
    """
    with open(filename, mode='r+',  encoding='utf-8') as f:
        my_list = f.readlines()
        for idx in range(len(my_list)):
            if (my_list[idx].find(search_string)) != -1:
                my_list.insert(idx + 1, new_string)
    with open(filename, mode='a',  encoding='utf-8') as f:
        f.write(str(my_list))

	XL2T11A
