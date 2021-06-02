#!/usr/bin/python3
""" Only Subclass of """


def inherits_from(obj, a_class):
    """function that returns True if the object
     is an instance of a class that inherited
      (directly or indirectly) fron the specified
      class"""
    return isinstance(obj, a_class) and obj.__class__ is not a_class
