#!/usr/bin/python3

"""
function to add two numbers and intercept error values
"""


def add_integer(a, b=98):
    """
    add two numbers a and b, also catch errors
    :param a: integer or float
    :param b: integer or float
    :return: sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("a must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        return int(a) + int(b)
    return a + b
