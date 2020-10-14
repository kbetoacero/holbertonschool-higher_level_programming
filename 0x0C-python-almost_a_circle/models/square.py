#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class the inherits for Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instatiation Square """

        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)
