#!/usr/bin/python3

"""
Define a class Square that represents a square.
"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (number, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Check if the area of the current square is greater than the other square."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Check if the area of the current square is greater than or equal to the other square."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Check if the area of the current square is less than the other square."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Check if the area of the current square is less than or equal to the other square."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

