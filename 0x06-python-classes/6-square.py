#!/usr/bin/python3

"""
Defines a square class that can be printed using my_print
"""

class Square:
    """
    defines a square
    """

    def __init__(self, x=0, position=(0, 0)):
        if not isinstance(x, int):
            raise TypeError('size must be an integer')
        if x < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = x
        self.size = x

    def area(self):
        """
        current area
        Return: area
        """
        return self.size * self.size

    def size(self, value=None):
        """
        changes _Square__size to size
        """
        if value is None:
            return self.size
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def __setattr__(self, key, value):
        """
        checks value of size
        :key: instance
        :value: value
        """
        if key != '_Square__size' and key == "size":
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__dict__[key] = value
        else:
            self.__dict__[key] = value

    def my_print(self):
        """
        prints a square of #
        """
        if self.size == 0:
            print()
        elif self.size == 1:
            print("#")
        else:
            s = "#" * self.size
            for _ in range(self.size):
                print(s)