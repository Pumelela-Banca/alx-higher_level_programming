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
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.size}"


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
