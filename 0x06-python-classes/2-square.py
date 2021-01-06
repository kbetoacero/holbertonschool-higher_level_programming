#!/usr/bin/python3
"""Script for class Square that defines a square """


class Square:
    """ private class method size,
        instantiation and define a square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
