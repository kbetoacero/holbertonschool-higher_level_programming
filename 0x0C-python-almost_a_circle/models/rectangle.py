#!/usr/bin/python3
""" Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle
        instance """
        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout the Rectangle
        instance with the caracter # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " " + "#" * self.__width)

    def __str__(self):
        """ method that returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height> """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.__x,
                                                 self.__y,   self.__width,
                                                 self.__height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each atttribute """
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.__width = args[arg]
                if arg == 2:
                    self.__height = args[arg]
                if arg == 3:
                    self.__x = args[arg]
                if arg == 4:
                    self.__y = args[arg]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """return the dictionary representation"""
        new_dictionary = {}
        new_dictionary['id'] = self.id
        new_dictionary['width'] = self.width
        new_dictionary['height'] = self.height
        new_dictionary['x'] = self.x
        new_dictionary['y'] = self.y
        return new_dictionary

