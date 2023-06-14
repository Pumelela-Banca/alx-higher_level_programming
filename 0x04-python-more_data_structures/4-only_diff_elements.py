#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    only_diff_elements - difference in two sets
    @set_1: 1
    @set_1: 1
    Returns: new list with all elements not in both sets
    """
    if len(set_1) == 0:
        return list(set_2)
    elif len(set_2) == 0:
        return list(set_1)
    if len(set_1) == 0 and len(set_2) == 0:
        return []
    else:
        return list(filter(lambda x: x not in set_1, set_2))