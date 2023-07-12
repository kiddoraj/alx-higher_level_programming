#!/usr/bin/python3
""" Module that returns the dictionary description with a simpledata structure for a JSON serialization of an object"""
def class_to_json(obj):
    """
    Return the dictionary description of an object with a simple data structure for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes (list, dictionary, string, integer, boolean).

    Returns:
        dict: The dictionary description of the object.
    """
    description = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            description[attr] = value

    return description
