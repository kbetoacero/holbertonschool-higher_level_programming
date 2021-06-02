#!/usr/bin/python3
""" Integer Validator """


class BaseGeometry:
    """ Public instance method def area(self)"""
    def area(self):
        """ raise an exception with message area()
        is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates value
        name: always a string
        value: != a integer raise TypeError
        value: <= 0 raise ValueError"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
