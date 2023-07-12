#!/usr/bin/python3
""" Module that contains a function that writes to a text file"""
def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the text file to write to. Default is an empty string.
        text (str): The string to write to the file. Default is an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
