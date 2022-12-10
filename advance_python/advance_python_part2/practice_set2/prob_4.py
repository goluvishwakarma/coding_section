# Date: 06-01-2021
"""
    Question: 4
    write a program to filter a list of number which are divisible by 5.
"""


# def divisible_by5(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
#
# div_by_5 = lambda num: num % 5 == 0

lst = [4, 5, 90, 35, 75, 1, 0, 3, 10, 15]
# print("number which are divisible by 5: ", list(filter(divisible_by5, lst)))
# print("number which are divisible by 5: ", list(filter(div_by_5, lst)))

print(list(filter(lambda a: a % 5 == 0, lst)))
