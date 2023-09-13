#!/usr/bin/python3

# computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    return [list(map(lambda x: x**2, matrix[row])) for row in range(rows)]
