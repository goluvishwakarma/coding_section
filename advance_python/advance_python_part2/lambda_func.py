# Date: 05-02-2021
# Topic: lambda function.
"""
    lambda function:
    function created using an expression using 'lambda keyword'.
    syntax;
            lambda arguments: expression(can be used as a normal function)

    Example:
        square = lambda x: x * x
        square(6) ---> return 36

        sum = lambda a, b, c: a + b + c
        sum(2, 3, 4) ---> return 6

"""
# def func(a):
#     return a + 6

func = lambda a: a + 5
square = lambda x: x * x
sum = lambda a, b, c: a + b + c

x = 566
print(func(x))  # we can pass more than one arguments.
print("square: ", square(5))
print("summation: ", sum(2, 3, 4))
