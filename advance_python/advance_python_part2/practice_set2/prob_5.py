# Date: 06-01-2021
"""
    Question: 5
    write a program to find the maximum of the number in a list using the reduce function.
"""
from functools import reduce

# lst_sum = lambda a, b: a + b

lst = [1, 34, 2, 45, 4, 5, 9, 11, 21, 40, 22, 55, 0, -6, -1, 99, 6, 8, 7]
val = reduce(max, lst)  # it takes the argument sequentially
print(val)
