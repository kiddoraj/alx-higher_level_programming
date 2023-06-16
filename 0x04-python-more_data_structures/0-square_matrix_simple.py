#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Iterate over each element in the matrix and compute its square
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return new_matrix
