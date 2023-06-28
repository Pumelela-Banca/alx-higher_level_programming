#!/usr/bin/python3

"""
This is a class
"""


class Square:
    """
    defines a square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """
        current area
        Return: area
        """
        return self._Square__size * self._Square__size
