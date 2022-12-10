# Date: 01-01-2021
"""
    Topic: lambda_function: is one line function or in other languages anonymous_function
    lambda_function_used: , when we used only once function in our program,

    Syntax:
    lambda arguments : manipulate(arguments)

"""

# in_general way:
# def add(a, b):
#     s = a + b
#     return s

# in lambda_function:
add = lambda x, y: x > y  # here we made a function add and two parameter and return specific_operation
print(add(2, 4))


# def X(val):
#     return val[1]
#
# a = [(1000, 200), (-7, 5), (45, -12)]  # list of tuple
# a.sort(key=X)
# print(a)


# use of lambda_function in list sorting:
a = [(1000, 200), (-7, 5), (45, -12)]  # list of tuple
a.sort(key=lambda x: x[1])

print(a)
