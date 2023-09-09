#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # matrix rows == matrix length
    rows = len(matrix)
    # print rows
    for y in range(rows):

        # print columns
        colms = len(matrix[y])
        for x in range(colms):
            print("{}".format(matrix[y][x]), end=" ")
        print("{}".format("\n"))
