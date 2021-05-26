#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_maxbeginning(self):
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

    def test_maxmiddle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_maxend(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_allnegative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_oneelement(self):
        self.assertEqual(max_integer([1]), 1)


if __name__ == '__main__':
    unittest.main()
