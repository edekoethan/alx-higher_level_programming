#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_new_matrix = matrix.copy() #my new_matrix to preserve the old one

    for i in range(len(matrix)):
        my_new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (my_new_matrix)
