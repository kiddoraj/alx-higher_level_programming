#!/usr/bin/python3

class BaseGeometry:
	""" Class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
	""" A Rectangle class , inherits from BaseGemeetry"""
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
	""" Class square , inherits from Rectangle"""
    def __init__(self, size):
	    """"
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
