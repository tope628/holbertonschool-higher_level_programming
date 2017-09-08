#!/usr/bin/python3
""" JSON Module
"""


import json


def load_from_json_file(filename):
    """
     Args:
         filename (file): The first parameter.

     Returns:
        string: JSON string
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
