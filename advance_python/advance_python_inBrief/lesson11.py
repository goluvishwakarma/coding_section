# Date: 01-01-2021
# Topic: Bisect Module:
import bisect

number = 5
a = [11, 2, 34, 4, 16, 79, 34, 89, 9]

print(bisect.bisect(a, number))  # 'it will give the index_position' at where we have to insert the data.
bisect.insort(a, number)  # it will insert the data at right_position.
print(a)

# Quick Quiz: sort a number list without using sort()
