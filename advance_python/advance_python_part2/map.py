# Date: 05-01-2021
# Topic: map
"""
    *. map:
    map applies a function to all the items in an input_lst.
    syntax:
            map(function, input_lst)
            here in the place of the function can be a lambda function also


"""


def square(num):
    return num * num


# if we want to store the square of this lst item in another_lst
# method_1:
lst = [1, 2, 3, 4]
square_lst = []
for item in lst:
    square_lst.append(square(item))

print(square_lst)

# method_2:
print(list(map(square, lst)))  # NOTE: here we have to type_cast into a list
