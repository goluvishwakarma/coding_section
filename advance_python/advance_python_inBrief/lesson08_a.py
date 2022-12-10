# reduce function:
from functools import reduce


def sum_num(a, b):
    return a + b


lis1 = reduce(sum_num, [1, 2, 3, 4])
print("sum of number in list: ", lis1)
