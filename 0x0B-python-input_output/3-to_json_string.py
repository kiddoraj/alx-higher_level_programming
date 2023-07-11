#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object (string) to convert to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
