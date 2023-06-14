#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    new_in_list - copy string and replace element
    @idx: index to change in copy
    @element: change to
    """
    if idx >= len(my_list):
        return my_list
    if idx < 0 or idx > (len(my_list)):
        return _copy(my_list)
    else:
        new = _copy(my_list)
        new[idx] = element
        return new


def _copy(my_list):
    """
    _copy - copies a list and returns copy
    @my_list: list
    """
    if len(my_list) == 0:
        return []
    else:
        new = []
        for x in range(0, len(my_list)):
            new += [my_list[x]]
        return new
