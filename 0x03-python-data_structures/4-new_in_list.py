#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = list(my_list)
    if idx > len(my_list):
        return copy_list
    else:
        copy_list.remove(copy_list[idx])
        copy_list.insert(idx, element)
        return copy_list
