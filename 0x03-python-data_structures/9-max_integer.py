#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    max_integer - returns biggest integer in list
    @my_list: list
    """
    if len(my_list) == 0:
        return None
    big = 0
    for x in my_list:
        if x < big:
            continue
        big = x
    return big
