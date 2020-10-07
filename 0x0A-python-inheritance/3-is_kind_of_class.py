#!/usr/bin/python3
"""
Module to test an obj to see which class
it belongs to or is inherited
"""


def is_kind_of_class(obj, a_class):
    """ True is obj is an instance or
    inherited from a_class. False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
