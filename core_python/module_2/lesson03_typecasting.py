# Date: 11-01-2021
# Topic: type() and type-casting in python:

"""
    *. type():
    type() is used to find the data_type of a given variable in python.

    *. type_casting:
    a datatype can be converted into another datatype.

    a numeric can be converted into a string and vice versa(possibly).
    e.i, "23" --- int("23"), here string_literal is converted into numeric_literal(string to integer conversion)

"""
int_var = 3454
str_var = "3454"  # NOTE: here "33454" is a string_literal and 3454 is numeric_literal.

# print(str_var + 5)  # it will throw an error, because we cannot add a string and integer

print(int(str_var) + 5)  # here we 'try to do type_casting' to 'str into int'

str_variable = "2324cast"
# type_castVar = int(str_variable)  # NOTE: here it will throw error


# ......and we can do same as with other data_type, so on
print(type(int("23")))
