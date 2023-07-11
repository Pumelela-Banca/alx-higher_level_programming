#!/usr/bin/python3

"""
a module with class that inherits from BaseGeometry and adds
init that adds width and height to base geometry
"""


class BaseGeometry:
    """
    has method that raises exception
    """

    def area(self):
        """
        not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Looks to validate integers
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))


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
