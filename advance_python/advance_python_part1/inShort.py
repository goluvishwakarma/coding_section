# Date: 05-01-2021, (ADVANCE_PYTHON),  author: @golu_vishwakarma

"""
    Exception Handling In Python,
    There are many built-in exception which are raised in python when something goes wrong.
    Exception in python can be handled using 'try' statement, the code that handles the exception is written in the
    except clause.
    ------ syntax:
    try:
        # code                                ---> code which might throw Exception
    except Exception as e:
        print(e)

    when the exception is handled, the code flows continuous without program interruption.
    -------------------------------------------------------------------------------------------------------------------

"""

# try-except, demo:
while True:
    print("press 'q' to quit")
    user_input = input("Enter a number: ")

    if user_input == 'q':
        break  # here our program will be exit
    try:
        print("Trying....")  # here it will be trying
        type_cast = int(user_input)
        if user_input > 9:
            print("You entered a number greater than 9")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")
