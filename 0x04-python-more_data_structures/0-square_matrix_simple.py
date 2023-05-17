#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    else:
        new_matrix = []
        for list_matrix in matrix:
            new_matrix.append(list(map(lambda x: x * x, list_matrix)))
        return new_matrix
