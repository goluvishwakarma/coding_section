# Date: 05-01-2021
# Topic: global_variable:

"""
    global keyword:
    global keyword is used to modify the variable outside of the current scope.

"""
a = 54  # global_variable


def func1():
    global a  # use global_variable
    print(f"print_statement 1: {a}")
    a = 4  # here we change the global_variable data, (NOTE: if we doesn't use global keyword then it will be local_var)
    print(f"print_statement 2: {a}")


func1()
print(f"print_statement 3: {a}")  # output will be 4
