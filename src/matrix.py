from fractions import Fraction
def to_matrix(values: list, width: int, height: int, default=None):
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Invalid width. Width must be a positive integer.")

    if not isinstance(height, int) or height <= 0:
        raise ValueError("Invalid height. Height must be a positive integer.")

    if len(values) != width * height:
        raise ValueError("Invalid number of values. The length of values should be equal to width * height.")

    matrix = []
    for i in range(height):
        row = []
        for j in range(width):
            index = i * width + j
            value = values[index] if index < len(values) else default
            row.append(value)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        row_str = " ".join(str(value) for value in row)
        print(row_str)

def inverse_matrix(matrix: list):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Invalid matrix. The matrix must be square.")
    if len(matrix) == 1:
        return [[Fraction(1, matrix[0][0])]]
    return multiply_matrix_by_scalar(cofactor_matrix(matrix), Fraction(1, determinant(matrix)))


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Invalid matrix. The matrix must be square.")
    if len(matrix) == 1:
        return Fraction(matrix[0][0])
    if len(matrix) == 2:
        return Fraction(matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1])
    det = Fraction(0)
    for i in range(len(matrix)):
        det += matrix[0][i] * cofactor(matrix, 0, i)
    return det


def cofactor_matrix(matrix):
    co_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(cofactor(matrix, i, j))
        co_matrix.append(row)
    return co_matrix


def cofactor(matrix, row, col):
    return ((-1) ** (row + col)) * determinant(minor(matrix, row, col))


def minor(matrix, row, col):
    return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]


def multiply_matrix_by_scalar(matrix: list, scalar: Fraction):
    return [[scalar * value for value in row] for row in matrix]