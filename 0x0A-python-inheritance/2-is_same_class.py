#!/usr/bin/python3

"""
function checks if class is subclass of another
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is
    exactly an instance of the specified class ;
    otherwise False
    """
    if isinstance(obj, a_class) and \
            a_class.__name__ != object.__name__:
        return True
    else:
        return False
