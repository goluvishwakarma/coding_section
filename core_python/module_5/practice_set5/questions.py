# Date: 13-01-2021
# ----------------- Question on dictionary and set:

# Question 1:   write a program to create a dictionary of hindi words with values as their english translation.
# provide user with an option to look it up!

my_dict = {
    "sabdkosh": "dictionary",
    "pustak": "book",
    "bhasha": "language",
    "khubsurti": "beauty",
    "likhawat": "scripting"
}
print("hindi words are: ", my_dict.keys())

# user_input = input("Enter hindi word as above mentioned to know english_meaning: ")
# print("english translation is: ", my_dict.get(user_input))


# Question 2:   write a program to input eight numbers from the user and display all the unique number(once).

# mySet = set()  # here we create a n emptySet
# for n in range(0, 8):
#     number_input = int(input("Enter number " + str(n + 1) + ": "))
#     mySet.add(number_input)
#
# print("unique numbers are: ", mySet)


# Question 3:   can we have a set with 18(int) and "18"(str) as a value in it.

s = {23, "23", 23, 23.0}  # Important
print(s, "set length: ", len(s))

#  Question 4:  st = {}, what is the type of st?  Ans. dict_type

st = {}
print("st type is: ", type(st))


# Question 5:   create an empty dictionary, allows 4 friends to enter their favourite language as values and use
# keys as their names, assumes that the names are unique.

lang_dict = {}

for i in range(0, 4):
    print("for friend "+str(i + 1))
    name_input = input("Enter your name: ")
    language_input = input("Enter your favourite language: ")
    lang_dict[name_input] = language_input

print("favourite language dictionary: ", lang_dict)


# Question 6:   can we change the given below data.
# s = {2, 3, 4, [34, -1, 0, 6, 7], 0, 1}
