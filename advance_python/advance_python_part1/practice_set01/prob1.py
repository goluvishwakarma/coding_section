# Date: 05-01-2021
"""
    Question:
    Write a program to open three files '1.txt', '2.txt' nd '3.txt'. If any of these files are not present,
    a message without existing the program must be printed prompting the same.

"""


def readFile(file_name):
    try:
        with open(file_name, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File '{file_name}' is not found")


readFile("1.txt")
readFile("21.txt")
readFile("3.txt")
