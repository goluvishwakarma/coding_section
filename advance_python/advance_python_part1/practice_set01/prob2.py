# Date: 05-01-2021

"""
    Question:
    Write a program to print 3rd, 5th and 7th element from a list 'using enumeration function'.
"""

lst = [1, 34, 0, None, "python", "java", "html", -6, 6, False]
for index, ele in enumerate(lst):
    if index == 2 or index == 4 or index == 6:
        print("element at index", index + 1, ":", ele)
