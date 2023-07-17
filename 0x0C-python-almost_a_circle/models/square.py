#!/usr/bin/python3

"""
a class that describes all attributes of a square
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    a square class derived from Rectangle with __str__ method changed
    """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self,size, size, x=x, y=y, id=id)
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.size}"

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.validate(value, "size")
        self.__height = value

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))