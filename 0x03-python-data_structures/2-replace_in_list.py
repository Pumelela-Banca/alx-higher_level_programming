#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replace_in_list - replace element at idx
    @my_list: list
    @idx: index
    @element: replace with
    """

    if len(my_list) == 0 or idx < 0:
        return my_list
    elif len(my_list) < (idx + 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
