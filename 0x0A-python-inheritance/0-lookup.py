#!/usr/bin/python3

"""Gets all the methods of all object
"""


def lookup(obj):
    """
    looks and prints all methods of object
    :param obj: class object
    :return: list with all methods
    """
    try:
        issubclass(object, obj)
    except TypeError:
        raise TypeError("Not class")
    all_meth = []
    for x in obj.__dict__.keys():
        all_meth.append(x)
    return all_meth
