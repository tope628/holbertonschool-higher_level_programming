#!/usr/bin/python3
""" JSON Module
"""


import json


def save_to_json_file(my_obj, filename):
    """
     Args:
         my_obj (object): The first parameter.
         filename (file): The second parameter.

     Returns:
        string: JSON string
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
