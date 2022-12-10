# Date: 05-01-2021
"""
    Question:
    Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the
    ZeroDivisionError.
"""
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

try:
    result = a / b
    print("result is: ", result)
except:
    print("Infinite")
