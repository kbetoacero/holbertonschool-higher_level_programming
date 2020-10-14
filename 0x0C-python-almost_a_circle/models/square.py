#!/usr/bin/python3
""" Rectangle class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class the inherits for Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instatiation Square """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        keys = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
