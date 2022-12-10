# Date: 11-01-2021
# string_problems:

# Question 1:   write a python program to display a user entered name followed by 'good morning' using input().
name = input("Enter your good name: ")
print("good morning, " + name)  # here we concatenate the name with prompt


# Question 2:   write a python program to fill in a letter template given below with name and date.
#           letter = ''' Dear <name>, You are selected! <date>
date = input("Enter the date: ")
letter = '''Dear '''+name+''',
greeting from abc coding house. I am happy to tell you about your selection
You are selected! 
have a great day ahead!
thanks and regards,
bill
'''+date+''''''

print(letter)


# Question 3:   write a python program to detect double spaces in a string.
str_var = "detect double spaces in   a string"
doubleSpaces = str_var.find("  ")

print("doubleSpaces is detected at index: ", doubleSpaces)


# Question 4: write a python program replace the doubleSpaces with a single space in question 3.
withSingle_space = str_var.replace("   ", " ")
print("after replacing doubleSpaces with single space: ", withSingle_space)

# Question 5:   write a program to format the following letter using escape sequence character.
# letter = "Dear golu, This python notes is nice. Thanks!

letter1 = "Dear golu, This python notes is nice. Thanks!"
print("\nbefore format the later is:\n", letter1)

formatted_letter = "Dear golu,\n\tThis python notes is nice.\n Thanks!"
print("after formatted the letter is:\n", formatted_letter)


