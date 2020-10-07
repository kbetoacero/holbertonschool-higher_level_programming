#!/usr/bin/python3
"""
class Square that inherits a class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """ instantiating square
        """
        self._size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Overriding str function
        """
        return "[Square] {}/{}".format(self._size, self._size)
