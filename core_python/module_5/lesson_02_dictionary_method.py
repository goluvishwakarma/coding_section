# Date: 13-01-2021
# Topic: ------------------- Dictionary Method:

my_dict = {"fast": "In a Quick manner",
           "python": "Is a programming_language",
           "marks": [67, 89, 98],
           "anotherDict": {"dict": "dict_within_a_dict"},
           1: 4

           }

print("content in the dictionary are: ", my_dict)

print("dictionary_keys: ", my_dict.keys())  # return list_containing keys
print("dictionary_values: ", my_dict.values())  # print the dictionary_values

print(type(my_dict.keys()))  # it will give the data_type
print(type(my_dict.values()))
print("type_casting in list: ", list(my_dict.keys()))  # type_cast

print(my_dict.items())  # iterating key-value pairs
# print the (key, value) for all contents of the dictionary

update_dict = {
    "book": "python_3 by orally",
    "java": "james gosling",
    "py_create": "guido van rossum",
    "marks": [67, 89, 98, 45.7]
}

my_dict.update(update_dict)  # here update(), update the dictionary with supplied key-value pairs.
print("updated_dictionary is: ", my_dict)  # adds at the end

print(my_dict.get("python"))  # prints values associated with key "python"
print(my_dict['python'])  # prints values associated with key "python"

""" the difference between .get() and [] syntax in dictionary """
print(my_dict.get("python2"))  # it return None as python2 is not present in the dictionary
# print(my_dict['python2'])  # throws an error as python2 is not present in the dictionary


"""  to know more about dictionary_method, go 'python.org.docs python dictionary_method'  """
