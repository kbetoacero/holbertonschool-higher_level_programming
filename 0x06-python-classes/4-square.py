#!/usr/bin/python3
"""Script for class Square that defines a square """


class Square:
    """ private instance atribute size """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ returns square's area """
        return self.__size * self.__size
