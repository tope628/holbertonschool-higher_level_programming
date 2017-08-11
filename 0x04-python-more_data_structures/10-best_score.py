#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    new_tup = my_dict.items()
    new_list = list(max(new_tup))
    return new_list[0]
