#!/usr/bin/python3

"""
module with class that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry methods and adds __init__
    """
    def __init__(self, width, height):
        __height = height
        __width = width
        self.integer_validator("'Rectangle'", __width)
        self.integer_validator("'Rectangle'", __height)
