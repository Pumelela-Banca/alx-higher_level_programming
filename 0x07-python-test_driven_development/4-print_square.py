#!/usr/bin/python3

"""
function prints square according to given constraints
"""


def print_square(size):
    """
    function that prints a square with the character #
    :param size: length of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(0, size):
        print("#" * size)
