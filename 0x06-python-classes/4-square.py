#!/usr/bin/python3

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
        self.size = self._Square__size

    def area(self):
        """
        current area
        Return: area
        """
        return self._Square__size * self._Square__size

    def size(self, value=None):
        """
        changes _Square__size to size
        """
        if value is None:
            return self.size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = value
