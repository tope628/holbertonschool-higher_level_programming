#!/usr/bin/python3
"""MyList  Module
"""
class MyList(list):
""" class that inherits ffrom list object """
	
    def print_sorted(self):
     """
     Args:
         self (object): The first parameter.

     Returns:
         list: sorted list.
    """
        print(sorted(self))
