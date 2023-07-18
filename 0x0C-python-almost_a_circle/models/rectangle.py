#!/usr/bin/python3

"""
Module documentation: Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate of the rectangle.
            y (int): Y coordinate of the rectangle.
            id (int): ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.

        Args:
            value (int): Value to set as the width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        Args:
            value (int): Value to set as the height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x attribute.

        Args:
            value (int): Value to set as the x coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y attribute.

        Args:
            value (int): Value to set as the y coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area value of the Rectangle instance.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with the character '#' in stdout,
        taking into account the x and y coordinates.
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: String representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle instance.

        Returns:
            dict: Dictionary representation of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
