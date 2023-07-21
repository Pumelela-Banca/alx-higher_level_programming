#!/usr/bin/python3

"""
Tests for rectangle class and its methods
"""

import unittest

from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    """test start"""
    def test_init(self):
        box = Rectangle(3, 4, 6, 3, 4)
        self.assertEqual(box.width, 3)

        self.assertEqual(box.id, 4)
        self.assertEqual(box.height, 4)
        self.assertEqual(box.x, 6)
        self.assertEqual(box.id, 4)

    """test setter"""
    def test_getter_setter(self):
        box = Rectangle(1, 2)
        self.assertEqual(box.width, 1)
        self.assertEqual(box.height, 2)

        # test x
        box = Rectangle(1, 2, 3)
        self.assertEqual(box.width, 1)
        self.assertEqual(box.height, 2)
        self.assertEqual(box.x, 3)

        # test y
        box = Rectangle(1, 2, 3, 4)
        self.assertEqual(box.width, 1)
        self.assertEqual(box.height, 2)
        self.assertEqual(box.x, 3)
        self.assertEqual(box.y, 4)
        # test id
        box = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(box.width, 1)
        self.assertEqual(box.height, 2)
        self.assertEqual(box.x, 3)
        self.assertEqual(box.y, 4)
        self.assertEqual(box.id, 5)

    """test errors"""
    def test_errors(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

    """test negative"""
    def test_negatives(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    """test zero x and y"""
    def test_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    """test area"""
    def test_area(self):
        self.assertEqual(Rectangle(2, 2).area(), 4)

        self.assertEqual(Rectangle(2, 2).area(), 4)


if __name__ == '__main__':
    unittest.main()