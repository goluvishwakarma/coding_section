# Date: 05-01-2021,
# Topic: try with else

"""
    try with else:
    try:
        # code
    except:
        # some_code
    else:
        # code                          ---> this is executed only if the try was executed
"""

try:
    i = int(input("Enter a number: "))
    c = 3/i
except Exception as e:
    print(e)
else:
    print("we were successful")  # here else statement will be execute only if the try block was executed.

