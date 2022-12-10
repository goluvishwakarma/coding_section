# Date: 13-01-2021
# Topic: List

"""
    *. list:
    list are containers to store a set of values of any data_type.
    NOTE: we create list using [](square_brackets)

    *. list methods:



"""
# here we create a list name as lst, using [] called square_bracket, 'remember that lst_indexes starts with 0 to n-1.'
lst = [2, 4, 8, 9, 0, 1, 3, 5]
print("list elements are: ", lst)

print("element at index_position[3]: ", lst[3])

lst[3] = 34  # here we change the value at index_position [3]
print("element updated at index_position[3] is 34: ", lst[3])  # NOTE: lst are mutable(...we can change the data)

print("updated lst is: ", lst)

# create a list with multiple data_type:
my_lst = [0, "anjali", 3.4, 'a', None, True, 2 + 4j, 3j]  # here 2 + 4j is complex_number
print("data in the lst are: ", my_lst)


# ---------- list_slicing in python:
print(lst[0:3])
print(my_lst[2:4])
print(lst[:])  # it will print the whole lst

# ---------- list_methods in python:
lst.sort()  # arrange the data in ascending to descending order
print("sorted lst is: ", lst)

my_lst.reverse()
print("reversed list is: ", my_lst)

lst.append(44)  # adds 44 at the end of the list
print("appended list is: ", lst)

my_lst.insert(3, "insert_ele")  # adds the "insert_ele" at index_position 3
print("inserted element in the list is: ", my_lst)

lst.pop(2)  # remove element at index_position 2
print("popped lst is: ", lst)

my_lst.remove('insert_ele')  # remove the 'insert_ele' from the list
print("removed element in the my_lis is: ", my_lst)

lst.copy()
print("copy the lst: ", lst)

lst_a = [2]  # it also a list with single element
print("lst_a with single_element: ", lst_a)
