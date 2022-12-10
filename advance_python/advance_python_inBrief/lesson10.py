# Date: 01-01-2021
# Topic: Advanced list Slicing(subset):

lis = [2, 4, 6, 7, 9, 5, -3, 0, 1, 8]
print(lis[1:3])  # Note: number of elements, 3 - 2: 1
print(lis[1:32])  # No Error!!!

# -ve slicing:
print(lis[-1:-5])  # it will give empty_list
print(lis[-5:-1])  # NOTE: it will be confused
print(lis[:-2])

# both, +ve nd -ve slicing:
print(lis[:-2])
print(lis[0:8])  # both will give same result

# ===========NOTE,
print(lis[::2])  # it will print the element after leave 1 element
print(lis[::1])  # it will print the exact_list

print(lis[::-1])  # IMPORTANT-NOTE: IT WILL REVERSE THE LIST

print(lis[2::3])  # start with index_[2] nd print the element after the skipping next two element
