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
        self.__size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y}" + \
            f"- {self.__size}"

    def update(self, *args, **kwargs):
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

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)