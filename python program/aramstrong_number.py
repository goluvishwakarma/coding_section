# 22.03.21

# Armstrong number
# 153:  1^3 + 5^3 + 3^3: 1 + 125 + 27

num = int(input("Enter a number: "))  # 153
length = len(str(num))  # length: 3

is_sumEqual = 0
copy_num = num


while copy_num != 0:  # 153, 15, now num = 0, hence condition is false
    rem = copy_num % 10  # 153 %1 0: 3, 5, 1
    is_sumEqual += rem ** length  # 0 + 3^3: 27, 27 + 5^3: 152, 152 + 1^3: 153
    copy_num //= 10  # 15, 1, 0

print(is_sumEqual)
if is_sumEqual == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")



