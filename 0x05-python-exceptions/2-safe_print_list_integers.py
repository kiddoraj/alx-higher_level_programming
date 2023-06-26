#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count < x:
                try:
                    print("{:d}".format(element), end=" ")
                    count += 1
                except ValueError:
                    pass
            else:
                break
        print()
        return count
    except:
        raise
