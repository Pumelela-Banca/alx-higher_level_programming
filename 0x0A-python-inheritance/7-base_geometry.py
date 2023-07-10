#!/usr/bin/python3

"""
a module with class to define geometry
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
            raise TypeError("{} must be greater than 0".format(name))
