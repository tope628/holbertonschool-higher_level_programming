#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    keys = sorted(my_dict.keys())
    for key in keys:
        print("{:s}: {}".format(key, my_dict.get(key)))
