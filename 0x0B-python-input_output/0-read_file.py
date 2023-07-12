#!/usr/bin/python3
""" Module that contains a function that reads from a file """
def read_file(filename=""):
    """
    Read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the text file to be read. Default is an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents, end='')
