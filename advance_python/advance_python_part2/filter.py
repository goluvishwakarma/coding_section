# Date: 05-01-2021
# Topic: filter

"""
    *. filter:
    filter creates a list of items for which the function 'returns true'.
            list(filter(function), list)
             here in the place of the function can be a lambda function also

"""


# normal_func:
def greater_then5(num):
    if num > 5:
        return True
    else:
        return False


# lambda_func:
g10 = lambda num: num > 10

lst = [1, 2, 3, 4, 5, 7, 9, 76, 99, 34, -7]
print(list(filter(greater_then5, lst)))
print(list(filter(g10, lst)))
