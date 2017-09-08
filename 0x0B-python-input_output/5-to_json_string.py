#!/usr/bin/python3
""" JSON Module
"""


import json


def to_json_string(my_obj):
    """
     Args:
         my_obj (object): The first parameter.

     Returns:
        string: JSON string
    """
    return json.dumps(my_obj)
