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
                (self.id, self.x, self.y, self.size))
