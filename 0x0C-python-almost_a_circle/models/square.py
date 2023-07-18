#!/usr/bin/python3

"""
Module documentation: Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for Square class.

        Args:
            size (int): Size of the square.
            x (int): X coordinate of the square.
            y (int): Y coordinate of the square.
            id (int): ID of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): Value to set as the size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square instance.

        Returns:
            dict: Dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
