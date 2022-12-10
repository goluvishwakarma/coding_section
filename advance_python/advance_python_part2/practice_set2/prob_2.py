# Date: 06-01-2021
"""
    Question: 2
    Write a program to input name, marks and phone_number of a student and format it using the format function
    like below.

    "the name of the student is name his marks are marks and phone number is phone_number"
"""
name = input("Enter name of the student: ")
marks = int(input("Enter the marks of the student : "))
pho_number = int(input("Enter the phone number of the student: "))

template = "the name of the student is {0} his marks are {1} and phone number is {2}"
output = template.format(name, marks, pho_number)

print(output)  # Output: the name of the student is golu his marks are 92 and phone number is 123232432463289

# NOTE: {} is called place_holder
