#!/usr/bin/python3
""" Module Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Rectangle Class that
    inherits for Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation of Rectangle class
        with private intance attributes """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
