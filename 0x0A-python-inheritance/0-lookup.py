#!/usr/bin/python3

"""Gets all the methods of all object
"""


def lookup(obj):
    """
    looks and prints all methods of object
    :param obj: class object
    :return: list with all methods
    """
    if type(obj) != type:
        raise TypeError("obj must be class type")
    all_meth = dir(obj)
    return all_meth
