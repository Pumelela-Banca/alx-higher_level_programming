#!/usr/bin/python3

"""
Class that defines a rectangle and its methods will be added
gradually

"""


class Rectangle:
    """
    Class defining rectangle with height and width
    """

    def __init__(self, width=0, height=0):
        """
        Initializer of instances
        :param width: width of rectangle
        :param height: height of rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height
        self._Rectangle__width = width

    @staticmethod
    def setup(name, value):
        """
        checks validity of name input
        :param name: name of side
        :param value: int value of side
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __setattr__(self, key, value):
        """
        checks value of size
        :key: instance
        :value: value
        """
        if key != '_Rectangle__height' and key == "width":
            Rectangle.setup(key, value)
            self.__dict__['_Rectangle__width'] = value
        elif key != '_Rectangle__height' and key == "height":
            Rectangle.setup(key, value)
            self.__dict__["_Rectangle__height"] = value
        else:
            self.__dict__[key] = value

    def area(self):
        """
        area of rectangle
        :return: area
        """
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        """
        perimeter of rectangle
        :return: perimeter
        """
        return 2 * (self._Rectangle__height + self._Rectangle__width)
