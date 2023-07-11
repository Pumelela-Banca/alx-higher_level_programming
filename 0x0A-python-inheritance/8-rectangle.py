#!/usr/bin/python3

"""
a module with class that inherits from BaseGeometry
and adds init that adds width and height
"""


class Rectangle(BaseGeometry):
    """
    a class inherits from BaseGeometry methods and adds __init__ with
    width and height
    """

    def __init__(self, width, height):
        __height = height
        __width = width
        self.integer_validator("'Rectangle'", __width)
        self.integer_validator("'Rectangle'", __height)
