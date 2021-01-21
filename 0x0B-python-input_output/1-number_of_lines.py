#!/usr/bin/python3
""" Number of lines """


def number_of_lines(filename=""):
    """ that returns the number of
    lines of a text file """
    count = 0
    with open(filename) as textfile:
        for i in textfile.readlines():
            count += 1
    return count
