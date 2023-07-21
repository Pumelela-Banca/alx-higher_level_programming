#!/usr/bin/python3

"""
Tests for square class and its methods
"""

import sys
import unittest
from io import StringIO

from models.square import Square


class TestSquare(unittest.TestCase):

    """test start"""
    def test_init(self):
        box = Square(4, 6, 3)
        self.assertEqual(box.size, 4)
        cc = box.id
        self.assertEqual(box.id, cc)
        self.assertEqual(box.x, 6)

    def test_type_vals(self):
        """tests type values"""
        with self.assertRaises(TypeError) as e:
            Square("2", 2, 2, 2)
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            Square(2, "2", 2, 2)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            Square(2, 2, "2", 2)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_attributes(self):
        """test negative attributes"""
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            Square(1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            Square(1, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """test area"""
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(2).area(), 4)

    def test_zero(self):
        """test zero x and y"""
        with self.assertRaises(ValueError) as e:
            Square(0, 2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_print_res(self):
        """test print results"""
        result = StringIO()
        sys.stdout = result
        print(Square(2))
        resu_str = result.getvalue()
        self.assertEqual(resu_str, "[Square] (26) 0/0- 2\n")
        sys.stdout = result

if __name__ == '__main__':
    unittest.main()