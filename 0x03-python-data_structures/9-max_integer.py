#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list == None:
        return None
    max_num = 0
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num
