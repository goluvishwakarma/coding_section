# Date: 05-01-2021
# Topic: try except finally:

"""
    try with finally:
    python offers a finally clause which ensures execution of a piece of code irrespective of the exception.

    try:
        # code
    exception:
        # code
    finally:
        # code                  ---> executed regardless of error.

"""

try:
    i = int(input("Enter a number: "))
    res = 4/i
    print(res)
except Exception as e:
    print(e)
    exit()
finally:
    print("we are done")

print("thanks for using the code")