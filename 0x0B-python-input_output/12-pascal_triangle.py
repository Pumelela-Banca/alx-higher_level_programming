#!/usr/bin/python3

"""
module contains a pascal triangle making function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        pass

