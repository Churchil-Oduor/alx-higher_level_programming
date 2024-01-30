#!/usr/bin/python3

"""This module contains a function
that divides a matrix's element by a
number passed as function parameter"""


def matrix_divided(matrix, div):
    """This function does the matrix elements division
    by div

    Args:
        matrix : the matrix whose elements are to
        be divided.

        div (int): number to divide each matrix element.

    Returns: new matrix which is a result of division
    of each matrix element with div.
    """
    new_matrix = []
    width = 0
    for element in matrix:
        width = width + 1

    if width == 0:
        return matrix

    try:
        width_check = 0
        for row in matrix:
            new_row = []
            for colm in row:
                width_check = width_check + 1
                if type(colm) not in [int, float]:
                    message = ("""matrix must be a
                    matrix (list of lists) of integers/floats""")
                    raise TypeError(message)

                colm = round(colm / div, 2)
                new_row.append(colm)
            new_matrix.append(new_row)
            length_difference = width_check - width - 1
            if length_difference != 0:
                raise TypeError("""Each row of the
                        matrix must have the same size""")
            width_check = 0

    except ZeroDivisionError:
        print("division by zero")
    except TypeError:
        print("Each row of the matrix must have the same size")
    return new_matrix
