#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                try:
                    result = dividend / divisor
                except ZeroDivisionError:
                    result = 0
                    print("division by 0")
                except TypeError:
                    result = 0
                    print("wrong type")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                result_list.append(result)
    except:
        raise
    finally:
        return result_list
