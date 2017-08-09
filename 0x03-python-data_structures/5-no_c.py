#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    my_list = [i for i in my_string if i != 'c' and i != 'C']
    copy_string = "".join(my_list)
    return copy_string
