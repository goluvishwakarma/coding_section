# Date: 15-01-2021
# ---------- question on conditional expression;

# Question 1:   write a program to find greatest of 4 numbers entered by the user.

lst = []
#
# for n in range(0, 4):
#     number = int(input("Enter number " + str(n + 1) + ": "))
#     lst.append(number)
#

# small = lst[0]
# for i in len(lst):
#     if lst[i] > small:
#         small = lst[i]
#
# print(str(small) + " is greatest number")

# if lst[0] > lst[3]:
#     g1 = lst[0]
# else:
#     g1 = lst[3]
#
# if lst[1] > lst[2]:
#     g2 = lst[1]
# else:
#     g2 = lst[2]
#
# if g1 > g2:
#     print(str(g1) + " is greatest number")
# else:
#     print(str(g2) + " is greatest number")

# Question 2: Calculate a student percentage

mark_lst = []
total = 0
for m in range(0, 3):
    marks_input = int(input("Enter your obtained mark in subject"+str(m + 1))+": ")
    total += marks_input
    mark_lst.append(marks_input)

# print(len(mark_lst))
if mark_lst[0] < 33 or mark_lst[1] < 33 or mark_lst[2] < 33:  #
    print("you are fail because you have less than 33% in one of the subject!")
elif round(total / 3, 2) < 40:
    print("you are fail due to total percentage is less than 40%")
else:
    print("congratulation! You passed the exam \
    \ntotal obtained mark: ", total, " and percentage is: ", round(total / 3, 2), "%")

# Question 3:
