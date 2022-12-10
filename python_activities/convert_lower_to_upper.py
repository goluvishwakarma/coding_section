# Date: 11-01-2021

# Question: 1   write a python program to convert a lower_case alphabet into upper_case without using method.
# Question: 2   write a python program to generate a lst which contain alphabet A-Z or a-z.
# Question: 3   write a python program to swap two number.

# Q - 1:
# user_input = input("Enter an alphabet in lower_case: ")
user_input = 'q'
print(user_input.upper())
print("entered lower_case alphabet converted into upper_case is: ", chr(ord(user_input) - 32))

# Q - 2:
alphabet_lst = []
for alpha in range(65, 91):
    # print(chr(alpha), end="  ")  # here we print alphabet A-Z
    alphabet_lst.append(chr(alpha))

print("generated lst is: ", alphabet_lst)

# Q - 3:
x = 3
y = 6
print("Before swapping: ")
print("the value of x: ", x, "and value of y: ", y)
x, y = y, x

print("After swapping: ")
print("the value of x:", x, " and value of y:", y)





