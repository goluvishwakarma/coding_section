# Date: 03-01-2021

# while_logic:
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# another while_logic: which will be quite confusing, but it has also the same_result.
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

for i in range(-1, 1):
    print("#")

num = []
val = num[:]
num.append(1)

print(val)
print(len(num))
print(len(val))

l = [0 for i in range(1, 3)]
print(l)

lst = [0, 1, 2, 3]
x = 1
for i in lst:
    x *= i
print(x)


def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


happy_new_year(1)

happy_new_year()
