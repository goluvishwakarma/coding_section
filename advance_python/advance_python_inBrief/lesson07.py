# Date: 01-01-2021
"""
    Topic:
    1. List Comprehensions
    2. Dictionary Comprehensions
    3. Generators Comprehensions
                                            """
# 1. List Comprehensions:
# here we made a list and create a newList from existing in which data is divisible by_3, in normal_way
list_1 = [23, 1, 34, 5, 6, 7, 9, 56, 89, 39, 20, 11, 12]
divide_by_3 = []

for item in list_1:
    if item % 3 == 0:
        divide_by_3.append(item)

print("Without Using List Comprehensions: ", divide_by_3)

# using list_comprehension,
print("Using List Comprehensions: ", [item for item in list_1 if item % 3 == 0])

# 2. Dictionary Comprehensions:
dict1 = {'a': 23, 'b': 45, 'A': 45}
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})
# Output: {'a': 68, 'b': 46}


# 3. Set Comprehension:
squared = {x ** 2 for x in [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]}
print(squared)

# 4. Generator Comprehension:
gen = (i for i in range(56) if i % 3 == 0)  # it will generate value on the fly
# here initialize the value
for item in gen:
    print(item, end=" ")
