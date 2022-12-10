# -------- Date: 06.12.20 ---------

# import math

# evaluate cubic square_root of the number through user_inout:

# user_input = float(input("Enter a number: "))
# print(type(user_input))
# print(math.sqrt(user_input ** 3))

# NOTE: input("Enter a number:") Here, whatever input() function takes, that will be string.
# so, we have to type_cast to achieve desire output.

# -------- Date: 08.12.20
# swapping:
"""
    there are lot of procedure to solve a particular problem, but solution is ONE
    in swapping, there is something like as it is swapping of two number,
    Here we'll be discuss 4 procedure to solve that problem. """

# swapping using temp_var:
x = 23
y = 11
print(f"before_swapping the values of: x: {x} and y: {y}")

temp = x  # here we store the value of  x_var in temp_var
x = y  # assigning the value of y_var in x_var
y = temp  # here we, assigning temp_var to y_var, (in temp_var the value of x is already assigned ).
print(f"after_swapping using temp_var: x: {x} and y: {y}")

# swapping using arithmetic operator:
x1 = 23
y1 = 11

y1 = x1 + y1  # y1: 23 + 11 = 34
x1 = y1 - x1  # x1: 34 - 23 = 11
y1 = y1 - x1  # y1: 34 - 11 = 23
print(f"after_swapping using arithmetic_operator: x: {x} and y: {y}")

# swapping using XOR:

a = 23
b = 11

a = a ^ b
b = a ^ b
a = a ^ b
print(f"swapping using_XOR: a: {a} and b: {b}")

# swapping using python, we can also say magic of python:

x2 = 23
y2 = 11

x2, y2 = y2, x2  # here we just assigning the value of x2 in y2 and value of y2 in x2.
print(f"after_swapping using python: x: {x2} and y: {y2}")

# prime check:

""" 
    1st of fall, we have to know what is prime number,
    : a number which has only 2 divisor 
    1st prime_number: 2
    here 2 is divisible by p.jpg and itself(i,e: 2), acc. to definition it's satisfied.
    9 is not a prime number because it's has more than two divisor. """

# pr_num = int(input("Enter a integer: "))
pr_num = 9  # we know that, it is not a prime number
count = 0  # here we initialize the variable, count with 0

for i in range(1, (pr_num + 1)):
    if pr_num % i == 0:
        count = count + 1  # here count_var count the divisor

if count == 2:
    print(pr_num, " is a prime number")

else:
    print(pr_num, " is not a prime number")

# __________ Fibonacci series:
""" 
    a series in which each term is sum of previous two term.
    0      +       p.jpg      +       p.jpg     +       2      +        3       +      5        +     ...
    a              b          c(a + b)      c1(c + b)      c2(c + c1)             """

up_to = 9
# up_to = int(input("Enter how many term you want to print: "))
a = 0
b = 1
print(f"fibonacci_series uo_to {up_to}: ")
print(a, end=" ")
print(b, end=" ")
for i in range(1, up_to - 1):
    c = a + b
    a = b
    b = c
    print(c, end=" ")

print("\n")
# _____________ Armstrong Number:
"""
    A number in which sum of cube of each digit of that number is equal to that number.
    153, 370, 371, 407 etc. are some armstrong_number.
    
    153 = p.jpg^3(p.jpg) + 5^3(125) + 3^3(27): p.jpg + 125 + 27 = 153 performed_operation is satisfied """

num = 370  # is a armstrong_number
match_isEqual = num  # here we stored the value of num into, another match..var
sum_isEqual = 0
count = 0
while match_isEqual != 0:
    rem = match_isEqual % 10  # 153 % 10 = 3 (% - gives remainder)
    sum_isEqual = sum_isEqual + (rem ** 3)  # 0 + 3^3 = 27  (^ - it will raised to power 3)
    match_isEqual //= 10  # 153 // 10 = 15 (//- integer division - gives quotient)
    count += 1  # it will count the operation, acc. to condition, (i.e. digits)

print(f"number of digits present in the number: {count}")
if num == sum_isEqual:
    print(num, " is a armstrong-number")

else:
    print(num, " is not an armstrong_number")

# ______________ Factorial :
"""
    n! = n * (n - p.jpg) * (n - 2) * (n - 3) * ....
    5! = 5 * 4 * 3 * 2 * p.jpg * 0: 120
    NOTE: 0! = p.jpg                 """

# number = int(input("Enter a integer number: "))
number = 5

fact = 1
for i in range(1, number + 1):
    fact *= i

print(f"factorial of {number}! is: {fact}")

# ______________Palindrome Check:

n1 = 4334
n = n1
store = 0

while n != 0:
    rem = n % 10  # 121 % 10: p.jpg
    store = 10 * store + rem  # 10 * 0 + p.jpg: p.jpg
    n = n // 10  # 121 // 10: 12, this process will be going until the condition is failed.

if store == n1:
    print("number is palindrome")

else:
    print("number is not palindrome")

# _______________Reversing a number:

# suppose we have a number 234, the output will be 432

number = 234
temp_var = number
rev_number = 0

while number != 0:
    rem = number % 10  # 234 % 10: 4
    rev_number = rev_number * 10 + rem  # [1st iteration]0 * 10 + 4: 4, [2nd iteration]4 * 10 + 3: 43
    number //= 10
    '''
         234 // 10: 23, now the number become 23 so whatever operation will be perform now in number 23 and
         so on in every iteration until the condition is true, NOTE: here (//) called floor or integer division  '''

print(f"before reversing the number: {temp_var}")
print(f"after reversing the number: {rev_number}")

# _____________Check a number is even or not without using % operator:
# 2(even_number): 0 without using % operator

N = 56  # which is even_number
even_check = N // 2  # it will store the quotient

if even_check * 2 == N:  # 1 * 2 == N(2): true(1)
    print(1)
else:
    print(0)

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
# 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1

''' tomorrow_task(11)-- print the pattern

    *             * * * * *
    * *             * * * *
    * * *   --->      * * *
    * * * *             * * 
    * * * * *             *         '''
# star_pattern using for_loop:
for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

# another_way to print star_pattern using for nd while_loop:
for i in range(0, 5):
    j = 0
    while j < i + 1:
        print("** ", end="")
        j += 1
    print()

#  creating in list:
List1 = [120, 4, 1, 4, 6, 0]
List2 = [32, 12, 2]

print("result is: ", int(List1 > List2))  # output will be true(1) nd false(0), here we doing type_cast
print(List1[1:-1])

# solution_11 star_pattern:
i = 0  # here we initialize the variable_i
n = 5
while i < 5:
    j = 0  # here we initialize the variable_j
    n -= 1
    while j < n + 1:
        print("* ", end="")
        j += 1
    print()  # it will take the cursor in NewLine after each iteration.
    i += 1

'''
* * * * *               *               * * * * *
  * * * *             * * *             * * * * 
    * * *           * * * * *           * * *
      * *         * * * * * * *         * *
        *       * * * * * * * * *       *
        
'''
# n = 5, 5 rows, " ", n - 1
# for i in range(0, 5):
#     for j in range(0, i - 1):
#         for k in range(0, j + 1):
#             print(" ", end="")
#         print("* ", end="")
#     print()

# ---------------- :here we are going to take n no. of user_input and print sum nd average of these number:
# n = int(input("Enter the number of term: "))
# store = 0
#
# for i in range(0, n):
#     numbers = int(input(f"Enter the number {i}: "))
#     store += numbers
#
# print("sum of these number is: ", store)
# print("average of these number is: ", (store / n))

# print, 5 * nd in nextLine print a whiteSpace preceding then print 4 star

x = (1, 2, 3,)

print(sum(x, 3))  # here x


