#!/usr/bin/python3
""" class My List
"""


class MyList(list):
    """ MyList that inherits
     from list """

    def print_sorted(self):
        """ Print List of int
        ascending order """
        print(sorted(self))
