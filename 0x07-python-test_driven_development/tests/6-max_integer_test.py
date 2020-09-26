#!/usr/bin/python3
"""Test module for max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Subclass of unittest.TestCase to run tests on
    max_integer function.
    """
    def test_for_docstring(self):
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([2]), 2)

    def test_negative(self):
        self.assertEqual(max_integer(list(range(-10, 0))), -1)
        self.assertEqual(max_integer([-1, 10, 3, 2, 1, 99]), 99)

    def test_max_sorted(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_desorted(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
