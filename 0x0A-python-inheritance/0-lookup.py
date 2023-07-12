#!/usr/bin/python3
"""  returns the list of available attributes
and methods of an object
"""

def lookup(obj):
    """

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the available attributes and methods.
    """
    return dir(obj)
