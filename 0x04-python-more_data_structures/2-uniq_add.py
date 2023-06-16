#!/usr/bin/python3
def uniq_add(my_list=[]):
    #use set and sum with map and lambda to add unique intergers
    result = sum(set(map(lambda x: x , my_list)))

    return result
