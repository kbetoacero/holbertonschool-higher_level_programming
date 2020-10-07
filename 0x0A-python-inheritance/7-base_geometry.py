#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """ empty class
    """
    def area(self):
        """ Area public instance
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Object that validates integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
