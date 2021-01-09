#!/usr/bin/python3

""" function to add 2 integers """


def add_integer(a, b=98):

    """ adds two integers a and b
    >>> add_integer(2, 98)
    100
    >>> add_integer(-2, 98)
    96
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
