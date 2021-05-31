#!/usr/bin/python3
""" Function thar reads
a file """


def read_file(filename=""):
    """ read a text file (UTF-8)
    and print to stdout
    """
    with open(filename, encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
