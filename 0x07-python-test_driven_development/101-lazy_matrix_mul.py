#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix multiplication.
    """
    return np.matmul(m_a, m_b)
