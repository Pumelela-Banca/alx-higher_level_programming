#!/usr/bin/python3
"""
module with a class with attributes width, y, height and x and inherits
from base
"""

from models.base import Base


class Rectangle(Base):
    """
    class inherits from Base and adds new attributes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init that adds to Base init, these attributes
        height, width, y and x
        Attributes:
            __width: width
            __height: height
            __x: x
            __y: y
            id: id
        """
        super().__init__(id=id)
        self.validate(height, "height")
        self.validate(width, "width")
        self.validate(y, "y")
        self.validate(x, "x")
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @height.setter
    def height(self, value):
        """setter for height"""
        self.validate(value, "height")
        self.__height = value

    @width.setter
    def width(self, value):
        """setter for width"""
        self.validate(value, "width")
        self.__width = value

    @x.setter
    def x(self, value):
        """setter for x"""
        self.validate(value, "x")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y"""
        self.validate(value, "y")
        self.__y = value

    def alt_set(self, key, value):
        """validator used in setters"""
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
        """calculates and returns area"""
        return self.__width * self.__height

    def validate(self, attr, name):
        """validator with exceptions"""
        if type(attr) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == "x" or name == "y":
            if attr < 0:
                raise ValueError(f"{name} must be >= 0")
        elif name == "width" or name == "height":
            if attr <= 0:
                raise ValueError(f"{name} must be > 0")

    def display(self):
        """display function that uses ##"""
        size = "#" * self.__width
        if self.__x == 0:
            for _ in range(0, self.__height):
                print(size)
        else:
            spc = " " * self.__x
            for _ in range(0, self.__height):
                print(spc, size)

    def __str__(self):
        """default printer"""
        return f"[Rectangle] ({self.id}) {self.__x}" + \
            f"/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        updates the attributes or changes them
        """
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

    def to_dictionary(self):
        """Turns attributes into a dictionary"""
        return dict(id=self.id, width=self.width, height=self.height,
                    x=self.__x, y=self.__y)
