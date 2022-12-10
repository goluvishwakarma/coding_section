# Date: 01-01-2021, program to print a number which is divisible by 1 to 10.

i = 1
while i > 0:
    j = i
    if j % 1 == 0 and j % 2 == 0 and j % 3 == 0 and j % 4 == 0 and j % 5 == 0 and j % 6 == 0 \
            and j % 7 == 0 and j % 8 == 0 and j % 9 == 0 and j % 10 == 0:
        print(j)
        exit()
    i = i + 1


