# Date: 01-01-2021
# Topic: Enumerate Function:

a = ["CodeWithGolu", "T-shirt", "Python", "java", "android"]

# suppose we have to print the 2nd_index data, then what will be do,
# i = 0
# for item in a:
#     i = i + 1
#     if i % 2 == 0:
#         print(item)

for i, item in enumerate(a):  # here i stands for index nd item stands for data
    if (i + 1) % 2 == 0:
        print(item)
