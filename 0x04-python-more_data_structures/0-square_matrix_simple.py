#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    #square = []
    square =[[row ** 2 for row in i] for i in matrix]
    return square
        
