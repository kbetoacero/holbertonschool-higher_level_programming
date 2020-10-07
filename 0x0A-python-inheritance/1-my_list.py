#!/usr/bin/python3
""" class My List
"""


class MyList(list):
    """ MyList that inherits
     from list """

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        self.list = self
        print(sorted(self.list))
