#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [row[:] for row in matrix]

    # Iterate through the rows and columns of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Square the value and assign it to the corresponding position in the result matrix
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
