# Date: 08/03/2021

# Note: how to print up to 2 decimal place in python

# num = 345.798956764839
# print("using format: {0:.2f}".format(num))
# print("using format specifier: %.2f" % num)
# print(round(num, 2))


# number = 123456
# sum_d = 0
# count = 0
#
# while number != 0:
#     num = number % 10  # 123456 // 10: 6, here 6 is stored in num
#     sum_d += num
#     count += 1
#     number = number // 10  # 123456 % 10: 12345, here number is now 12345
#
# print(sum_d, count)


# n = 123
# sum_of_digit = 0
# count = 0
#
# for digit in str(n):
#     count += 1
#     sum_of_digit += int(digit)
#
# print("sum of digit of a number is: ", sum_of_digit,
#       "and number of digits arr: ", count)


# SUM OF FIRST AND LAST DIGIT OF A NUMBER:


# n = input("Enter a integer number: ") # n:    12345
# print(f"sum of 1st and last digit of the number({n}) is: ", int(n[0]) + int(n[-1]))


oriNum = "12345"
revNum = oriNum[::-1]

print(int(oriNum) % 10 + int(revNum) % 10)


#  number:      12345, we have to calculate sum, 1st and last digit e.i, 1 + 5:   6,    sum = 0,
#  12345//10: 5, in 1st iteration, when number != 0  and store it in sum

