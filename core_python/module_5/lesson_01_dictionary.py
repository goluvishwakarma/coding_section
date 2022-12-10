# Date: 13-01-2021
# Topic: Dictionary

"""
    *. dictionary:
    dictionary is a collection of key-value pairs and unordered.
    Note, it is mutable.

    syntax:
            dict = { "key1": "valueA",
                     "key2": "valueB",
                     "key3": "valueC",
                     "key4": "valueD"
                    }  # here key1 print the value

    *. dictionary_property:
    1. It is unordered
    2. It is mutable
    3. It is indexed
    4. cannot contain duplicate keys

"""
# here we create a dictionary name as dict using {}, 'called curley_braces'
my_dict = {"Fast": "In a Quick manner",
           "Python": "Is a programming_language",
           "Marks": [67, 89, 98],
           "AnotherDict": {"dict": "dict_within_a_dict"}
           }  # NOTE: here we take the key_value as a string it can be also a _alphaNumeric

print("content in the dictionary are: ", my_dict)

print("key_value, Fast: ", my_dict['Fast'])  # way to access the particular key_value
print("Python, key_value: ", my_dict['Python'])

print("AnotherDict, key_value: ", my_dict['AnotherDict'])
print("dictionary's key_value within key_value: ", my_dict['AnotherDict']['dict'])

# update the dictionary:
my_dict['Python'] = "Is a purely object-oriented programming language"  # NOTE: 'dictionary is mutable'
print("updated value in dictionary is: ", my_dict)

# -------------- dictionary_methods:
