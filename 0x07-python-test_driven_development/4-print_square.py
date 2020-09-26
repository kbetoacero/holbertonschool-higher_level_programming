#!/usr/bin/python3
""" Print a square Module """


def print_square(size):
    """
    print_square
    Args:
        size : int
    Returns:
        None

    >>> print_square(4)
    ####
    ####
    ####
    ####

    """

    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float:
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("{}".format("#"*size))
        if i == size:
            break


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
