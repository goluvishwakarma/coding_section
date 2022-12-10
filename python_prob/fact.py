# Date: 31-12-20, By Golu
# in this python_program we calculate factorial of a number,

def userInput():
    number = int(input("Enter A Positive Integer Number: "))
    return number
    # NOTE: remember input(), always take input as a string


def factorial(n):
    fact = 1

    for i in range(1, (n + 1)):
        fact = fact * i

    # return fact
    return "The factorial of " + str(n) + " is: " + str(fact)
    # NOTE: here we have to type_cast the n ND fact, because we cannot add the string ND int type together


return_value = userInput()

if return_value < 0:
    print("Error!!!: Factorial of a negative number is not defined")
else:
    # print(f"factorial of {return_value} is: ", factorial(return_value))
    print(factorial(return_value))
