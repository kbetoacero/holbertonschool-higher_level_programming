#!/usr/bin/python3
"""class Rectangle that defines a Rectangle"""


class Rectangle:
    """ Rectangle class. """

    def __init__(self, width=0, height=0):
        """This is a function.
        Attributes:
        self (int): self.
        width (int): number.
        height (int): number.
        """
        self.height = height
        self.width = width

    def __str__(self):
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for i in range(0, self.__height):
            if i < self.__height - 1:
                s = s + ("#" * self.__width + "\n")
            else:
                s = s + ("#" * self.__width)
        return s

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
