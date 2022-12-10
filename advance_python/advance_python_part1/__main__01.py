# Date: 05-01-2021
# Topic: if __name__ == __main__
"""
    __name__ evaluates to the name of the module_1 in python from where the program is run.

    if the module_1 is being run directly from the command line, the __name__ is set to string "__main__"
    thus this behaviour is used to check whether the module_1 is ran directly or imported to another file.

"""


def greet(name):
    print(f"Happy New Year, {name}")
    # suppose this is very complicated function. nd we want to reuse this in another file


# print(__name__)
if __name__ == '__main__':
    n = input("Enter a name: ")
    greet(n)
