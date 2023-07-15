#!/usr/bin/python3

"""
module with classes rectangle and square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class that implements area, and uses size validator
    """
    def __init__(self, size):
        self._Square__size = size
        self.integer_validator('size', size)

    def area(self):
        return self._Square__size ** 2

    def __repr__(self):
        return self.area()

    def __str__(self):
        return f"[Square] {self._Square__size}/{self._Square__size}"
