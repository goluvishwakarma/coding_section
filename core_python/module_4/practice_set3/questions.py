# Date: 13-01-2021
# Question on list and tuple:

# Question 1:   write a python program to store seven fruit names through user_input.
fruit_lst = []  # here we create empty fruit list

print("Enter 7 fruits name")
for fruit in range(0, 7):
    user_input = input("Enter the fruit_name " + str(fruit + 1) + ": ")
    fruit_lst.append(user_input)

print("stored fruits are: ", fruit_lst)


# Question 2:   write a python program to accept marks of 6 student and display them in a sorted order.
mark_lst = []

for marks in range(0, 6):
    n = float(input("Enter the mark for student number" + str(marks + 1) + ": "))
    mark_lst.append(n)

mark_lst.sort()
print("marks of students in sorted order: ", mark_lst)


# Question 3:   write a python program to check tuple cannot be changed
my_tuple = (1, 21, 0, 0.0, 'a', 9, 7, "tuple_item")
# my_tuple[4] = A # throw na error, as we know it's Not allowed in python
print("tuple element are: ", my_tuple)


# Question 4:   write a program to sum a list with 4 number.
sum_lst = [1, 90, 7, 8]
add = 0
for i in sum_lst:
    add += i

print("sum of the list elements: ", add)
print("sum of the list elements using sum(): ", sum(sum_lst))  # NOTE,


# Question 5:   write a program to count the number of zeros in the following tuple.
# t = (7, 0, 8, 0, 0, 9)

tpl = (7, 0, 8, 0, 0, 9)
print("occurrence of 0 in the tuple is: ", tpl.count(0))

