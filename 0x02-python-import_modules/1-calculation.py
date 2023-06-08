#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5

    sum_result = add(a, b)
    diff_result = sub(a, b)
    prod_result = mul(a, b)
    quot_result = div(a, b)

print("{} + {} = {}".format(a, b, sum_result))
print("{} - {} = {}".format(a, b, diff_result))
print("{} * {} = {}".format(a, b, prod_result))
print("{} / {} = {}".format(a, b, quot_result))
