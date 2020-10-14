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
        """ Validation """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ Returns the area value of the
        rectangle instance """
        return (self.width * self.height)

    def display(self):
        """ Prints in stdout the Rectangle
        instance with the character # """
        if self.y > 0:
            print("\n" * self.y, end="")
        for i in range(self.height):
            if self.x > 0:
                print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ Returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assings an argument to each attribute """
        keys = ["id", "width", "height", "x", "y"]

        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
