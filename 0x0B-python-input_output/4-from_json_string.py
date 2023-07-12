#!/usr/bin/python3
""" Module that contains a function that returns an object by
a JSON representation"""
import json

def from_json_string(my_str):
    """
    Return the object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
