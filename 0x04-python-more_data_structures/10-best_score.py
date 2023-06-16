#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary: #checks if the dic is empty
        return None
    # max() finds the max key based on associate values
    return max(a_dictionary, key = a_dictionary.get) 
