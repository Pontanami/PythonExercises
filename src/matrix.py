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

def print_matrix(matrix: list, title: str = None):
    if title:
        print(title)
    for row in matrix:
        print(row)


def multiply_matrix_by_scalar(matrix: list, scalar: float):
    return [[scalar * value for value in row] for row in matrix]


def cofactor(matrix, param, i):
    c = []
    for row_index in range(len(matrix)):
        if row_index != param:
            row = []
            for col_index in range(len(matrix)):
                if col_index != i:
                    row.append(matrix[row_index][col_index])
            c.append(row)
    return (-1) ** (param + i) * determinant(c)


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Invalid matrix. The matrix must be square.")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    det = 0
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


def inverse_matrix(matrix: list):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Invalid matrix. The matrix must be square.")
    if len(matrix) == 1:
        return [[1 / matrix[0][0]]]
    return multiply_matrix_by_scalar(cofactor_matrix(matrix), 1 / determinant(matrix))

