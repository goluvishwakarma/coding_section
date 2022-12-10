# Date: 05-01-2021
# Handling Different Exception In Python:

"""
    we can also specify the exception to catch like below:
    try:
        # code
    except ZeroDivisionError:
        # code
    Except TypeError:
        # code
    except:
    # code                              ---> all other exceptions are handle here.

"""
try:
    a = int(input("Enter a number: "))
    c = 1 / a
    print(c)
# except Exception as e:  # here we are handling
#     print("Exception Occurred!!!")
#     print(e)  # NOTE: it will be print exception

except ValueError as e:
    print("Exception Occurred!!!")
    print("Please enter a valid number")

except ZeroDivisionError as e:
    print("Exception Occurred!!!")
    print("Make sure you are not dividing by 0")

except Exception as e:  # all other exception are handled, HERE
    print("Exception Occurred!!!")
    print(e)

print("Thanks for using this code!")

# NOTE: 2/0, here python automatically generate exception
