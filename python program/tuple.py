# Date: 24/02/2021, tuple use in python

""" DEFINITION:
a tuple is a collection which is ordered and immutable. in python tuple are written with round brackets, '()'. """
tpl = ("python", "java", "kotlin", "c language", "c++", "tuple", "orange", "pine_apple", "melon")
print("items are: ", tpl)


# ACCESSING TUPLE ITEMS: we can access tuple items by referring to the index number, inside square brackets, '[]'.
print("accessing the items through indexing: ", tpl[0], tpl[2], tpl[1])


# NEGATIVE INDEXING: in python, we can also accessing the items by -ve indexing,
# from -1 refers the last item, -2 refers to the second last item and so on.
print("accessing the items through -ve indexing: ", tpl[-1], tpl[-3], tpl[-2])


# RANGE OF INDEXES(SLICING): we can specify a range on indexes by specifying where to start and where to end the range,
# when specifying a range, the return value will be a new tuple with the specified items.
print(tpl[1:4])
print(tpl[-1:-3])  # Note
print(tpl[3:])
print(tpl[:5])
print(tpl[5:6])
print(tpl[:])
print(tpl[-5:-1])


# CHANGE TUPLE VALUESl:
# once a tuple is created, we cannot change its values, tuples are immutable
# but, we can convert 'the tuple into a list', 'change the list', and 'convert the list back into list'.
print("before changing the tuple items: ", tpl)
convert_lst = list(tpl)

convert_lst[3] = "change_the_tuple items"
convert_bkInto_tpl = tuple(convert_lst)

print("after changing the tuple items: ", convert_bkInto_tpl)

# reverse the tuple
print("reversing the tuple:\n", convert_bkInto_tpl[::-1])

