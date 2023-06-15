#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    common_elements - compares two sets and gets common element
    @set_1: 1
    @set_1: 1
    """
    if len(set_1) == 0:
        return {}
    elif len(set_2) == 0:
        return {}
    else:
        return list(filter(lambda x: x in set_1, set_2))
