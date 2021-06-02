#!/usr/bin/python3
""" Lookup Function"""


def lookup(obj):
    """ Function that returns the list of
    available attributes and methods
    of an object
    """
    return list(dir(obj))
