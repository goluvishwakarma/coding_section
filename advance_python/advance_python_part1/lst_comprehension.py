# Date: 05-01-2021
# Topic: list comprehension.
"""
    list comprehension:
    list comprehension is an elegant way to create lists based on existing lists.

    lstOne = [1, 5, 7, 3, 2, 6 , 0, 9]
    lstTwo = [i for i in lstOne if i > 4]
"""

# 1st_approach:
lst = [2, 9, 0, 5, 6, 4, 56, 78, 99, 3, 1, 11, 21, 12, 50, 33]
even_lst = []
for i in lst:
    if i % 2 == 0:
        even_lst.append(i)

print("collection of even_element: ", even_lst)


# 2nd_approach: shortcut to write the same_code:
even_lst = [i for i in lst if i % 2 == 0]
print("collection of even_element: ", even_lst)  # this approach,  we can also use for same as 'set' nd 'dictionary'

# lst_comprehension for set:
lst_a = [1, 2, 4, 4, 5, 8, 9, 1, 3, 3, 0, 7, 6, 6]
set_a = {i for i in lst_a}
print("element in set: ", set_a)


