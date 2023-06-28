#!/usr/bin/python3

"""
This is a module that defines a Square class.
"""

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self._size = size
