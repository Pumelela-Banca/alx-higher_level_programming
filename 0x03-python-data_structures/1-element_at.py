#!/usr/bin/python3

def element_at(my_list, idx):
    """
    element_at - returns item at index idx
    @my_list: list
    @idx: index
    """

    if len(my_list) == 0 or idx < 0:
        return None
    elif len(my_list) < (idx + 1):
        return None
    else:
        return my_list[idx]
