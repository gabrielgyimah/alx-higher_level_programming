#!/usr/bin/pythhon3

def print_matrix_integer(matrix=[[]]):
    for current_list in matrix:
        for num in current_list:
            print("{:d}".format(num), end=" ")
        print()
