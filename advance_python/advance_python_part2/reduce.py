# Date: 06-02-2021
# Topic: reduce
"""
    *. reduce:
    reduce applies a rolling computation to sequential pair of elements.

    from functools import reduce
    val = reduce(function, lst)
    here in the place of the function can be a lambda function also

    if the function computes sum of two number and the list is [1, 2, 3, 4]
    1st - 1 + 2: 3
    2nd - 3 + 3: 6
    3rd - 6 + 4: 10


"""
from functools import reduce

sum = lambda a, b: a + b

lst = [1, 3, 4, 2, 5, 7]
val = reduce(sum, lst)  # it add the elements in sequentially
print(val)
