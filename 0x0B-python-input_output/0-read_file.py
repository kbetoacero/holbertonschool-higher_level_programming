#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ reads a text file (UTF8)
    and prints it to stdout """

    with open(filename, encoding='utf8') as textfile:
        fde = textfile.read()
        print(fde, end="")
