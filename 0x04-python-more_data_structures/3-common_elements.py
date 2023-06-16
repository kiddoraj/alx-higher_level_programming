#!/usr/bin/python3
def common_elements(set_1, set_2):
    #Use set, filter and lambda to filter common elements
    common_set = set(filter(lambda x: x in set_1, set_2))

    return common_set
