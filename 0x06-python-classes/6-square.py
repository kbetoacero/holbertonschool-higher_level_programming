#!/usr/bin/python3
""" class square that defines
    a square """


class Square:
    """Class square that defines
    a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 integers')
        if all(value) < 0:
            raise TypeError('position must be a tuple of 2 integers')
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end='')
            for i in range(self.size):
                print("".join("{}".format(("_" * self.position[0])
                    + ("#" * self.size))))
