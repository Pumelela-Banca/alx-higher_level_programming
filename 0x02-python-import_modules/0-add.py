#!/usr/bin/python3

from add_0 import add

a = 1
b = 2

if __name__ == "__main__":
    print("{a} + {b}".format(a, b, add(a, b)))