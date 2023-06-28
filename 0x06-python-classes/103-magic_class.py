#!/usr/bin/python3
"""Define a class MagicClass that performs calculations based on radius."""


import math


class MagicClass:
    """
    Represent a MagicClass.

    Performs calculations based on the radius.
    """

    def __init__(self, radius=0):
        """
        Initialize a new MagicClass.

        Args:
            radius (float or int): The radius of the MagicClass.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
