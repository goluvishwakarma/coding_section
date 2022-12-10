# Date: 07-07-2022, author...

# sum of digit of a number:  number = 1234(input): 1 + 2 + 3 + 4:  10(output)
def sum_digit():
    number = 1234
    string = str(number)
    add = 0

    for i in string:  # string: "1234"
        add += int(i)

    return f"sum of digit of a number{number}: ", add


year = 1900

# year % 4 == 0 and year % 400 == 0
if year % 4 == 0 and year % 400 == 0:
    print("leap year")
else:
    print("not leap year")
account_no = "11116560458008"
pin = 2343

user_pin = int(input("Enter your pin code: "))
# cast_into_str = str(user_pin)

slice_code = account_no[4:8]

# print(slicing)
if pin == user_pin:
    print(account_no[0:4] + slice_code + account_no[8:14])
else:
    print("1111XXX58008")

# print(account_no[0:4]+slice_code+account_no[8:14])
