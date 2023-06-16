#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0  # Initialize a variable to store the count
    list_keys = list(a_dictionary.keys())  # Convert dictionary keys into a list

    for i in list_keys:  # Iterate over the list of keys
        num += 1  # Increment the count for each key

    return num  # Return the count
