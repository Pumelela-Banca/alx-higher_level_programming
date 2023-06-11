#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    divisible_by_2 - return all divisible by two
    @my_list: list
    Return: list with true or false at index
    """
    if len(my_list) == 0:
        return None
    new = []
    for x in my_list:
        if x % 2 == 0:
            new += [True]
        else:
            new += [False]
    return new
