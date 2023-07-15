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
        return [[]]
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1]]
    else:
        return pri_list(n)


def pri_list(new_l):
    """
    prints and returns new list
    """
    ll = [1, 1]
    new = []
    all_l = [[1], [1, 1]]
    for x in range(0, new_l - 2):
        for y in range(0, len(ll) + 2):
            if y == 0 or y == len(ll):
                new.append(1)
            elif y == len(ll) + 1:
                pass
            else:
                new.append(ll[y - 1] + ll[y])
        ll = new
        all_l.append(new)
        new = []
    return all_l
