# Date: 05-01-2021
# Topic: join_method.
"""
    join method:

    creates a string from iterable objects.
        lst = ["hii,", "how", "are", "you"]
        " and ".join(lst)
    the above line will return "hii, and how and are and you"


"""
lst = ["Camera", "Laptop", "Phone", "ipad", "Hard Disk", "Nvidia Graphics 3080 Card"]
sentence = " ,and, ".join(lst)  # here we can use "~~", "--" and so on.
print(sentence)
print(type(sentence))  # it will give the data_type
