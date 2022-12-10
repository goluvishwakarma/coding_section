# Python Program To Check Weather A Number Is A Palindrome Or Not,
# A number is said to be palindrome,if the reverse number is equal to that number.
# 121, 252, 313, ect. are palindrome_number.

# here we a take user_input
# print("type of the input: ", type(number))  # it will give the type of input
# number = int(input("Enter a number: "))  # here we type_cast the input, string to int
# temp = number
# reverse = 0
#
# while number != 0:
#     last_digit = number % 10  # 131 % 10: 1
#     reverse = reverse * 10 + last_digit  # a digit wil be append
#     number = number//10  # here we update the number
#
# if reverse == temp:
#     print(temp, " is a palindrome_number")
# else:
#     print(temp, " is not a palindrome_number")

# -------, check_palindrome using function:
def takeInput():  # take user_input
    number = int(input("Enter a integer number: "))
    return number


def isPalindrome(n):  # here we checking, number is palindrome or not
    rev = 0
    temp = n

    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    # if rev == temp:
    #     return True
    # else:
    #     return False
    return rev


num = takeInput()
# print(int(isPalindrome(num)))
reverse = isPalindrome(num)

if reverse == num:
    print("Number Is Palindrome")
else:
    print("Number Is Not A Palindrome")


