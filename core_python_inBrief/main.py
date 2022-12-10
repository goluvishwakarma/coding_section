# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# star_pattern:

i = 0  # here we initialize the variable_i
n = 8

while i < n:
    j = 0  # here we initialize the variable_j
    while j < i + 1:
        print("* ", end="")
        j += 1
    print()  # it will take the cursor in NewLine after each iteration.
    i += 1
    n -= 1
