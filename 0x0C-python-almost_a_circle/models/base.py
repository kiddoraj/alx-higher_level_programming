#!/usr/bin/python3

"""
Module documentation: Base
"""

import json
import csv
import turtle


class Base:
    """
    Base class for managing ID attributes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for Base class.

        Args:
            id (int): ID of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by the JSON string.

        Args:
            json_string (str): JSON string representation of a list of dictionaries.

        Returns:
            list: List represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            **dictionary: Dictionary of attributes.

        Returns:
            Base: Instance with attributes set.
        """
        dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                if json_data:
                    data = cls.from_json_string(json_data)
                    instances = [cls.create(**instance_data) for instance_data in data]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                next(reader)  # Skip header
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def to_csv_row(self):
        """
        Return the CSV representation of the instance.

        Returns:
            list: List representing the instance.
        """
        return [self.id]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open a window and draw all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        screen = turtle.Screen()
        screen.bgcolor("white")
        pen = turtle.Turtle()

        for rect in list_rectangles:
            pen.up()
            pen.goto(rect.x, rect.y)
            pen.down()
            pen.color("blue")
            pen.pensize(2)
            for _ in range(2):
                pen.forward(rect.width)
                pen.right(90)
                pen.forward(rect.height)
                pen.right(90)

        for square in list_squares:
            pen.up()
            pen.goto(square.x, square.y)
            pen.down()
            pen.color("red")
            pen.pensize(2)
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)

        turtle.done()
