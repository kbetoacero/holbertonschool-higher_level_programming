#!/usr/bin/python3
""" Prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """
    function to print name
    Args:
        first_name : the first name
        last_name : the second name
    Returns:
        None
    >>> say_my_name(2, "Acero")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string

    >>> say_my_name("Carlos", 12)
    Traceback (most recent call last):
    ...
    TypeError: last_name must be a string
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
