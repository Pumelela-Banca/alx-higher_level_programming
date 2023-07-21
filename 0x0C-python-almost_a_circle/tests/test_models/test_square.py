#!/usr/bin/python3

"""
Tests for square class and its methods
"""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):

    """test start"""
    def test_init(self):
        box = Square(4, 6, 3)
        self.assertEqual(box.size, 4)
        self.assertEqual(box.id, 20)
        self.assertEqual(box.x, 6)

    """test area"""
    def test_area(self):
        self.assertEqual(Square(2, 2).area(), 4)

    """test zero x and y"""

    def test_zero(self):
        with self.assertRaises(ValueError) as e:
            Square(0, 2)
        self.assertEqual(str(e.exception), "height must be > 0")



if __name__ == '__main__':
    unittest.main()