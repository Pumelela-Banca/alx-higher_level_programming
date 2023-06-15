#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    multiply_list_map - use map to multiply list
    @my_list: list
    @number: number to use
    """
    if len(my_list) == 0:
        return []
    return list(map(lambda x: x * number, my_list))
