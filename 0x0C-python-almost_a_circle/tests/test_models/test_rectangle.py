#!/usr/bin/python3

"""
Tests for rectangle class and its methods
"""

import sys
import unittest
from io import StringIO

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

    def test_area(self):
        """test area"""
        self.assertEqual(Rectangle(2, 2).area(), 4)
        self.assertEqual(Rectangle(2, 2).area(), 4)

    def test_print_res(self):
        """test print results"""
        result = StringIO()
        sys.stdout = result
        print(Rectangle(2, 3))
        resu_str = result.getvalue()
        self.assertEqual(resu_str, f"[Rectangle] (19) 0/0 - 2/3\n")
        sys.stdout = result

    def test_display(self):
        """test display method"""
        result = StringIO()
        sys.stdout = result
        Rectangle(4, 2).display()
        resu_str = result.getvalue()
        self.assertEqual(resu_str, "####\n####\n")
        sys.stdout = result

    def test_display_1(self):
        """test display method"""
        result = StringIO()
        sys.stdout = result
        Rectangle(4, 2, 4).display()
        resu_str = result.getvalue()
        line = "     ####\n     ####\n"
        self.assertEqual(resu_str, line)
        sys.stdout = result

    def test_to_dict(self):
        """test to dict return"""
        rr = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(rr, dict(width=1, height=2,
                    x=3, y=4, id=5))

    def test_update(self):
        """tests update"""
        rr = Rectangle(1, 3, 4, 25, 5)
        rr.update()
        vals = rr.to_dictionary()
        self.assertEqual(vals, dict(width=1, height=3,
                                    x=4, y=25, id=5))
        rr.update(33)
        self.assertEqual(rr.to_dictionary(), dict(width=1, height=3,
                                                  x=4, y=25, id=33))
        rr.update(33, 5)
        self.assertEqual(rr.to_dictionary(), dict(width=5, height=3,
                                                  x=4, y=25, id=33))
        rr.update(33, 5, 16)
        self.assertEqual(rr.to_dictionary(), dict(width=5, height=16,
                                                  x=4, y=25, id=33))
        rr.update(33, 5, 16, 2)
        self.assertEqual(rr.to_dictionary(), dict(width=5, height=16,
                                                  x=4, y=25, id=33))
        rr.update(33, 5, 16, 2, 4)
        self.assertEqual(rr.to_dictionary(), dict(width=5, height=16,
                                                  x=2, y=4, id=33))


if __name__ == '__main__':
    unittest.main()