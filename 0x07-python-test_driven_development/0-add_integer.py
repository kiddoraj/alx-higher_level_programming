#!/usr/bin/python3
"""
This module contains a function that adds two numbers.
"""

def add_integer(a: float, b: float = 98) -> int:
    """
    Adds two numbers and returns the result as an integer.

    Args:
        a (float): The first number.
        b (float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not a float or integer.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer.")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer.")
    
    return int(a) + int(b)
