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
        self.assertEqual(resu_str, "[Square] (30) 0/0- 2\n")
        sys.stdout = result

    def test_display_0(self):
        """test display method"""
        result = StringIO()
        sys.stdout = result
        Square(4).display()
        resu_str = result.getvalue()
        self.assertEqual(resu_str, "####\n####\n####\n####\n")
        sys.stdout = result

    def test_display_1(self):
        """test display method"""
        result = StringIO()
        sys.stdout = result
        Square(4, 2).display()
        resu_str = result.getvalue()
        line = '   ####\n   ####\n   ####\n   ####\n'
        self.assertEqual(resu_str, line)
        sys.stdout = result

    def test_to_dict(self):
        """test to dict return"""
        rr = Square(1, 3, 4, 5).to_dictionary()
        self.assertEqual(rr, dict(size=1,
                    x=3, y=4, id=5))

    def test_update(self):
        """tests update"""
        rr = Square(1, 3, 4, 5)
        rr.update()
        vals = rr.to_dictionary()
        self.assertEqual(vals, dict(size=1,
                                    x=3, y=4, id=5))
        rr.update(33)
        self.assertEqual(rr.to_dictionary(), dict(size=1,
                                                  x=3, y=4, id=33))
        rr.update(33, 5)
        self.assertEqual(rr.to_dictionary(), dict(size=5,
                                                  x=3, y=4, id=33))
        rr.update(33, 5, 16)
        self.assertEqual(rr.to_dictionary(), dict(size=5,
                                                  x=3, y=16, id=33))
        rr.update(33, 5, 16, 2)
        self.assertEqual(rr.to_dictionary(), dict(size=5,
                                                  x=2, y=16, id=33))
        rr.update(33, 5, 16, 2, 4)
        self.assertEqual(rr.to_dictionary(), dict(size=5,
                                                  x=2, y=16, id=33))


if __name__ == '__main__':
    unittest.main()