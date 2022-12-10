# date: 21.07.22,  @author...

# tech number: number of digits should be even, let 2025 number_digit: 4, 20 + 25: 45^2: 2025 == that number[2025]
# 2025: str: "2025
number = 2025
store = number

tostring = str(number)

length = len(tostring)
add = 0

if length % 2 == 0:
    slice_str = length // 2  # 4 // 2: 2
    add = int(tostring[0:slice_str]) + int(tostring[slice_str: (length + 1)])  # 2 + 2


print(add)
if (add ** 2) == number:
    print(number, "number is tech")
else:
    print(number, "number is NOT a tech")
