#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        space = ""
        for i in n:
            print("{:s}{:d}".format(space, i), end="")
            space = " "
        print()
