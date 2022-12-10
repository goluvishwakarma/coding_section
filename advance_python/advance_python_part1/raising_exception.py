# Date: 05-01-2021,
# Topic: raising_exception(custom_exception)
"""
    Raising Exception:
    We can raise custom exception using the 'raise keyword' in python.
"""


def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("this is not valid")  # here we generate our custom_message


# user_input = int(input("Enter a number: "))
# print("result: ", increment(user_input))
print("result: ", increment("hifife"))  # it will throw custom_error
