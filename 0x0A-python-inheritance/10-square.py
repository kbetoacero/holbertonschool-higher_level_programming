#!/usr/bin/python3
""" Square #1 """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square the inherits from
    rectangle"""
    def __init__(self, size):
        self.__size = size
        self.__width = size
        self.__height = size
        super().integer_validator("size", size)
        super().__init__(size, size)
