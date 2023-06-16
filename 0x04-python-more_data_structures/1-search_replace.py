#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #use map and lambda to create a new list with replced elements.
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
