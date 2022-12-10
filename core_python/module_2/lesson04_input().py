# Date: 11-01-2021
# Topic: input()

"""
    input():
    this function allows the user to take input from the keyboard as a string.

    NOTE:the output of the input is always a string (even if 'the number' is entered)
"""
user_input = input("Enter a name: ")

user_input = int(user_input)  # here we converted 'user_input' to a integer
print(type(user_input))


