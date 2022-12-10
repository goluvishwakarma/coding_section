# Date: 11-01-2021
# Topic: --------------- variable and data_type in python ---------------
# a variable is the name given to a memory location, e.i. 'named memory_location'

"""
    *. datatype ---- type of data
    *. variable ---- container to store a value
    *. keywords ---- reversed_word in python
    *. Identifiers ---- class/function/variable_name
    ------------------------------------------------------------------------------------------------------
    *. data_types:
    primarily there are following data types in python:
    1. Integer
    2. Floating point number
    3. String
    4. Booleans (True or False)
    5. None (to represent nothing)
    ------------------------------------------------------------------------------------------------------
    python is dynamical_type language, e.i it implicitly identifies the data_type
    we do not have to declare the data_type.
    ------------------------------------------------------------------------------------------------------

    *. rules for construct a variable_name:
    1. a variable name can only contain alphabet, digits and underscore(_).
    2. a variable name can only start with an alphabet and underscore(_).
    3. a variable name cannot star with a digit.
    4. no white space is allowed to be used inside a variable name.
    5. variable names are case_sensitive(a and A both are not same).

"""
var1 = 23  # by default it is integer
var2 = 'a'
var3 = 34.89
var4 = "name"
bool_var1 = True  # 1
bool_var2 = False  # 0

variable = """ "string" """
str_var = ''' 'another_string" '''
print(variable, str_var)

# printing the variable_type:

print(type(variable))  # it will give the data_type
