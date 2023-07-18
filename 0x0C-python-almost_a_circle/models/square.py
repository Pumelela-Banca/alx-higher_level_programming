#!/usr/bin/python3
"""
module with class that describes all attributes of a square class
taking attributes from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a square class derived from Rectangle with __str__ method changed
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Square init using size"""
        Rectangle.__init__(self,size, size, x=x, y=y, id=id)
        self.__x = x
        self.__y = y
        self.__size = size

    def __str__(self):
        """return details"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y}" + \
            f"- {self.__size}"

    def update(self, *args, **kwargs):
        """update"""
        if args and args is not None:
            try:
                self.id = args[0]
                self.__size = args[1]
                self.__y = args[2]
                self.__x = args[3]
            except IndexError:
                return
        else:
            for x in kwargs:
                self.alt_set(x, kwargs[x])

    def alt_set(self, key, value):
        if key == "size":
            self.validate(value, "width")
            self.__size = value
        elif key == "y":
            self.validate(value, "y")
            self.__y = value
        elif key == "x":
            self.validate(value, "x")
            self.__x = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.validate(value, "width")
        self.__size = value

    def to_dictionary(self):
        return dict(id=self.id, size=self.__size,
                    x=self.__x, y=self.__y)
