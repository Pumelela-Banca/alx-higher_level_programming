#!/usr/bin/python3

"""
module contains a base class tests matching
given questions
"""

import unittest

from models.base import Base


class TestSquare(unittest.TestCase):
    """test id track"""
    def test_ids(self):
        ints1 = Base()
        ints2 = Base()
        ints3 = Base(10)
        ints4 = Base(5)
        ints5 = Base()

        self.assertEqual(ints1.id, 1)
        self.assertEqual(ints2.id, 2)
        self.assertEqual(ints3.id, 10)
        self.assertEqual(ints4.id, 5)
        self.assertEqual(ints5.id, 3)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string("[]"), '"[]"')
        self.assertEqual(Base.to_json_string([{"id": 3}]), '[{"id": 3}]')
        self.assertEqual(Base.to_json_string('[{"id": 3}]'), '"[{\\"id\\": 3}]"')


if __name__ == '__main__':
    unittest.main()
