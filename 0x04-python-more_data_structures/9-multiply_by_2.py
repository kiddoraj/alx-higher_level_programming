#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {} #create new dic to store updated key values

    for key, value in a_dictionary.items(): #iterate over each key-value pair in the input dic
        new_dictionary[key] = value * 2

    return new_dictionary
