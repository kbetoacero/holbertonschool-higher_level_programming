#!/usr/bin/python3
""" Function to append to a file
"""


def append_write(filename="", text=""):
    """ Append a string into a file
    encoding UTF-8 an returns number of characters
    added
    
    :param filename: filename
    :param text: text
    :return: number of characters added
    """
    with open(filename, mode="a", encoding="UTF-8") as my_file:
        return my_file.write(text)
