# Date: 13-01-2021
# Topic: Tuple

"""
    *. tuple:
    tuple is an immutable data_type in python.
        immutable ---- cannot change
    once defined a tuple's element can't be altered or manipulate.


"""
# here we create a tuple name as tpl using (), called parenthesis
tpl = (1, 23, 0, 3, 6, 9, 4, 6, 5, 8, 2)
print("elements in the tuple are: ", tpl)

print("element at index_position tpl[4] is: ", tpl[4])

# tpl[5] = 34  # it will throw an error, 'Note: tuple are immutable( i.e, we cannot update the data).'

# tpl = ()  # an empty tuple
# tpl = (1)  # wring way to declare a tuple with single element, it will treated as a simple var_value
# tpl = (1,)  # tuple with single_element

""" --------- tuple_methods in python: """

my_tpl = (2, 0, 34, 11, 1, 2, 4, 8, 5, 3, 1, 2, 7, 9, 7, 00, 5)
print("count the specified element: ", my_tpl.count(2))  # it will return number of occurrence of value.

print("value at the specified index_position: ", my_tpl.index(5))  # it will return the value at that index_position

# to know more about tuple_methods, 'go python.org.docs tuple methods'.





