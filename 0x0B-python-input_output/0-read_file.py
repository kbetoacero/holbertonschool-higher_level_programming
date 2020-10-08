#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ reads a text file (UTF8)
    and prints it to stdout """
    count = 0
    with open(filename) as txtfile:
        for i in txtfile.readlines():
            count += 1
    return count
