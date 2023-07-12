#!/usr/bin/python3
""" Module that contains a function that appends to a text file"""
def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.

    Args:
        filename (str): The name of the text file to append to. Default is an empty string.
        text (str): The string to append to the file. Default is an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
