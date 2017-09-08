#!/usr/bin/python3
""" JSON Module
"""


import json


def from_json_string(my_str):
    """
     Args:
         my_str (object): The first parameter.

     Returns:
        string: JSON string
    """
    return json.loads(my_str)
