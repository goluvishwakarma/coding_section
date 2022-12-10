# Date: 06-01-2021
"""
    Question: 3
    a list contains the multiplication_table of 7. write a program to convert it to a vertical string of
    same numbers with exception-handling .

"""

try:
    num = int(input("Enter a number: "))
    lst = [str(num * i) for i in range(1, 11)]  # here we have to typCast lst into str otherwise it will go for
    # exception
    if lst == str:
        print(lst)
    ver_str_tab = "\n".join(lst)
    print(ver_str_tab)

except Exception as e:
    print(e)  # here exception will be handle

