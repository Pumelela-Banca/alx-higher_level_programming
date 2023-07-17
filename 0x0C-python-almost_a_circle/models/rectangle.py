#!/usr/bin/python3

"""
a module with attributes width, y, height and x and inherits
from base
"""

from base import Base


class Rectangle(Base):
    """
    class inherits from Base and adds new attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=id)
        self.validate(height, "height")
        self.validate(width, "width")
        self.validate(y, "y")
        self.validate(x, "x")
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x

    def __getattr__(self, item):

        if item == "width":
            return self.__dict__["__width"]
        elif item == "height":
            return self.__dict__["__height"]
        elif item == "y":
            return self.__dict__["__y"]
        elif item == "x":
            return self.__dict__["__x"]
        else:
            return self.__dict__[item]

    def __setattr__(self, key, value):

        if key == "width":
            self.validate(value, "width")
            self.__dict__["__width"] = value
        elif key == "height":
            self.validate(value, "height")
            self.__dict__["__height"] = value
        elif key == "y":
            self.validate(value, "y")
            self.__dict__["__y"] = value
        elif key == "x":
            self.validate(value, "x")
            self.__dict__["__x"] = value
        else:
            self.__dict__[key] = value

    def alt_set(self, key, value):
        if key == "width":
            self.validate(value, "width")
            self.__width = value
        elif key == "height":
            self.validate(value, "height")
            self.__height = value
        elif key == "y":
            self.validate(value, "y")
            self.__y = value
        elif key == "x":
            self.validate(value, "x")
            self.__x = value

    def area(self):
        return self.__width * self.__height

    def validate(self, attr, name):

        if type(attr) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == "x" or name == "y":
            if attr < 0:
                raise ValueError(f"{name} must be >= 0")
        elif name == "width" or name == "height":
            if attr <= 0:
                raise ValueError(f"{name} must be > 0")

    def display(self):
        size = "#" * self.__width
        if self.__x == 0:
            for _ in range(0, self.__height):
                print(size)
        else:
            spc = " " * self.__x
            for _ in range(0, self.__height):
                print(spc, size)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):

        if args and args is not None:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__y = args[4]
                self.__x = args[3]
            except IndexError:
                return
        else:
            for x in kwargs:
                self.alt_set(x, kwargs[x])

