# Date: 01-01-2-2021
"""
    , Map, Filter ND Reduce:

    1. Map function:
    syntax: map(function_to_apply, list of inputs)

    """


# in normal_way:
# list1 = [1, 2, 3, 4, 5]
# sq = []
#
# for item in list1:
#     sq.append(item**2)
# print(sq)


def square(n):
    return n ** 2


list1 = [1, 2, 3, 4, 5]
sq = list(map(square, list1))  # NOTE: here we type_cast the map to list
print(sq)


# Filter function:
def greater_than_2(n):
    if n > 2:
        return True
    else:
        return False


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, -3, -5, -1]
greaterThanTwo = list(filter(greater_than_2, list2))  # takes 1st argument as functionName nd 2nd argument as list
print(greaterThanTwo)   # Output: [3, 4, 5, 6, 7, 8, 9]

