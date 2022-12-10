# Date: 05-01-2021

"""
    Question:
    Write a 'list comprehension' to print a list which contains the multiplication_table of a user entered number.
"""
num = int(input("Enter the number: "))

lst = [num * i for i in range(1, 11)]
print("multiplication_table: ", lst)


