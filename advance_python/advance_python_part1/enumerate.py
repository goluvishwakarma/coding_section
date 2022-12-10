# Date: 05-01-2021
# Topic: enumerate function:
"""
    enumerate function:
    the enumerate function adds counter to an iterable and returns it

    for index, item in enumerate(list):
        print(index, item), -----> print the items of list with index_position.

"""

# if we also want to access the index with items, then, 1st_approach
lst = [3, 44, 7, 0, False, None, -2, "python"]
index = 0
for item in lst:
    print(f"item at index {index}: ", item)
    index += 1  # NOTE: 'index++' is not valid in python

# 2nd_approach:
for index, item in enumerate(lst):
    print("item at index", index, ":", item)

