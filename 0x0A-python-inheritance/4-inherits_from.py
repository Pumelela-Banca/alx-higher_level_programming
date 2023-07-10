#!/usr/bin/python3

"""
if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """
    if not isinstance(a_class, object):
        raise TypeError("c_class has to be a class")
    if a_class is object and obj is not object:
        return True
    elif obj is object and a_class is object:
        return False
    to_class = type(obj)
    return go_deep(to_class, a_class)


def go_deep(look, hey):
    """
    collects all super classes in a list and returns
    it
    """

    print(look.__base__, hey)
    if look.__base__ is None:
        return False
    else:
        if look == hey:
            return True
