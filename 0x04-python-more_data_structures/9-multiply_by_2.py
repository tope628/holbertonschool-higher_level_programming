#!/usr/bin/python3
def multiply_by_2(my_dict):
    dict2 = {}
    for k in my_dict.keys():
        dict2[k] = my_dict[k] * 2
    return dict2
