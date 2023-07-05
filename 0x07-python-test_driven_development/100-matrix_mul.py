#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Performs matrix multiplication on two matrices.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                   if an element of the matrices is not an integer or float,
                   or if the matrices are not rectangular.
        ValueError: If m_a or m_b is empty or if the matrices cannot be multiplied.

    Returns:
        list: Result of matrix multiplication.
    """

    # Validate m_a and m_b requirements

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    num_columns_m_a = len(m_a[0])
    if any(len(row) != num_columns_m_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    num_columns_m_b = len(m_b[0])
    if any(len(row) != num_columns_m_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if num_columns_m_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0] * num_columns_m_b for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(num_columns_m_b):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

