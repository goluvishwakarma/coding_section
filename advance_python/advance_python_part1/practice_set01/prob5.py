# Date: 05-01-2021
"""
    Question: 5
    Store the multiplication_table generated in problem 3 in a file named 'table.txt'.
"""

num = int(input("Enter the number: "))

lst = [num * i for i in range(1, 11)]
print("multiplication_table: ", lst)
with open("table.txt", "a") as f:
    f.write(str(lst))
    f.write('\n')