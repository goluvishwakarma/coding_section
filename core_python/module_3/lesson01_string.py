# Date: 11-01-2021
# Topic: ----------------- string in python -----------------

"""
    string:
    string is a data_type in python.
    string is a sequence of character enclosed in quotes.

    we can primarily write a string in these three ways.
    1. single quoted_string: 'hello'    2. double quoted_string: "hello"
    3. triple quoted_string: '''hello'''

    *. string_slicing:
    a string can be sliced for getting a part of that string
            name = "s  t  r  i  n  g", length is: 6
                    0  1  2  3  4  5       ----- +ve index
                   -6 -5 -4 -3 -2 -1       ----- -ve index

    *. index in a string starts from '0' to '(length - 1)' in python.
    NOTE: in python we can use both -ve and +ve indexing or slicing
    by the use of -ve index or slicing  we achieve the last part of that string

    *. Negative index: Negative indices can also be used as shown above. -1 corresponds to the (length - 1) index
    , -2 to (length - 2).

"""
a = 'hello'
b = "34"
print(a + b)

str_var = "string_variable's"
print(str_var)

variable = '''this is triple 
quoted string'''
print(variable)

# -------- :string_slicing:

greet = "good morning"
name = "anjali"
new_string = greet + name  # here we concatenating two string

print(new_string)
print("string_length: ", len(greet))

# ------- string_indexing:
print(name[0])
print(name[-3])  # NOTE: in python we can use both -ve and +ve indexing and also slicing.
# name[5] = "e"  # Not allowed, throw an error

# -------- slicing:
print(name[:4])  # is same as name[0:4]
print(name[0:])  # is same as name[0:5]
print(name[0:-4])



