#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        tup = (0, 0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        tup = ((tuple_a[0] + tuple_b[0]), 0)
    elif len(tuple_b) == 0 and len(tuple_a) == 1:
        tup = (tuple_a[0], 0)
    elif len(tuple_b) == 1 and len(tuple_a) == 0:
        tup = (tuple_b[0], 0)
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        tup = ((tuple_a[0] + tuple_b[0]), tuple_a[1])
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        tup = ((tuple_a[0] + tuple_b[0]), tuple_b[1])
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        tup = tuple_b
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        tup = tuple_a
    else:
        tup = ((tuple_a[0] + tuple_b[0]), (tuple_b[1] + tuple_a[1]))
    return tup
