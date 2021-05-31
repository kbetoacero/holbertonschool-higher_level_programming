#!/usr/bin/python3
""" Funtion thar writes a string to
a text file"""


def write_file(filename="", text=""):
    """
    write a file(UTF-8)
    :param filename: filename
    :param text: text
    :return: number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as my_file:
        return my_file.write(text)
