# Date: 13-01-2021
# Topic: Set in python

"""
    *. set:
    set is a collection of non repetitive elements in python.

    set(data_type) in python which contain 'unique values'


"""
# here we create a set name as st using {}, called curly_braces.
st = {1, 3, 4, 5, 2, 0, 4, 1, 6, 9, 0}

print("elements in the set are: ", st)
print("st type is: ", type(st))

# Important: this syntax will create an empty dictionary and not an empty set.
my_set = {}
print(type(my_set))

# an empty set can be created using the below syntax:
a_set = set()
print(type(a_set))

a_set.add(3)  # adding an element in the set
a_set.add(4)
a_set.add(4)  # adding a value repeatedly does not change a set
a_set.add(7)
a_set.add((1, 3, 2, 4, 5, 6, 7))  # but we can add a tuple

# a_set.add([3, 6, 0])  # it will throws an error, we cannot add list in set
# a_set.add({2: 6})  # we cannot also add a dictionary in set
print("a_set elements are: ", a_set)

# length of the set:
print("length of set: ", len(a_set))  # print the length of this set

# removal of an element:
a_set.remove(4)  # remove 5 from the set
# a_set.remove(34)  # throws an error while trying to remove 34(which is not present in the set)
print(a_set)

print(a_set.pop())  # removes an arbitrary element from the set and returns the element removed

# a_set.clear()  # empties the set
print(a_set)  # output: set()

"""
    *. set,union(): returns a new set with all items from both sets.
    
    *. set.intersection(): returns a set which contains only items in both sets.
"""

set_one = {2, 5, 3, 6, 0, 2.5, 7, 9, 1}
set_two = {0.0, 2, 1, 8, 4, 12, 0, 5, 1.2, 3}

print("union of the sets: ", set_one.union(set_two))
print("intersection of the sets: ", set_one.intersection(set_two))

# print(set_two.intersection(set_one))

print(0.0 == 0)  # NOTE, True
