#!/usr/bin/python3
""" Module tht contains a function
    that prints a square"""


def print_square(size):
    """ Function to pritn a square
    Args:
        size: int
    Returns:
        None

    >>> print_square(3)
    ###
    ###
    ###

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float:
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format("#"*size))
        if i == size:
            break


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
