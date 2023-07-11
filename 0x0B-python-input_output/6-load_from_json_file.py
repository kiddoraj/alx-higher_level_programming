#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
