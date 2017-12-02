#!/bin/python3
# finds a peak in a list of unsorted integers


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    mid = len(list_of_integers)//2
    peak = list_of_integers[mid]

    if ((mid == 0 or list_of_integers[mid - 1] <= peak) and
        (mid == len(list_of_integers) - 1 or
            list_of_integers[mid + 1] <= peak)):
        return peak

    elif (mid != len(list_of_integers) - 1 and
            list_of_integers[mid + 1] >= peak):
       return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid])


