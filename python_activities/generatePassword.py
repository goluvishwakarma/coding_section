import random  # here we import random module_1

lower = "abcdefghijklmonpqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-@#"

add_all_cha = lower + upper + numbers + symbols

length = 16   # here we specified the length of the password should be 16.
# here we generate random combination of character(password), in below line
password = "".join(random.sample(add_all_cha, length))

print(password)

string_input = str(input("Enter the above code:\n"))
'''
    Here we are checking, if the random_generated password(code) matched with user input then the
    a message will be show: correct code else in-correct code.  
    
'''
if password == string_input:
    print("Opened Page is,")
else:
    print("Enter correct code")


base_user_input = int(input("Enter the base: "))
exponent_user_input = int(input("Enter the exponent: "))

result = base_user_input ** (2 * exponent_user_input - 1)

print(f"exponentiation_result {base_user_input}^(2 * {exponent_user_input} - 1) is: ", result)
cast_in_string = str(result)  # here we casting the result into string, to get the result_length.
print("result_length: ", len(cast_in_string))


