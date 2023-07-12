#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""
def add_attribute(obj, attr, value):
    """

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
