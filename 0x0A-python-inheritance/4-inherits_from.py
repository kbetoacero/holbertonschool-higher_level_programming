#!/usr/bin/python3
""" test an object to see which class
    it belongs to or is inherited from
"""


def inherits_from(obj, a_class):
    """ Returns true or false id the object
    is an instance
    """
    return (isinstance(obj, a_class) and not (type(obj) is a_class))
