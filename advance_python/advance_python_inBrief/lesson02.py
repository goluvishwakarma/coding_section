# Date: 31-12-20,
# Topic: *args and **kwargs or *vars and **kvars

# in_normal way,
def function_1(name, age, rollNo):
    print("The name of the student is", name, "and age is", age, "and rollNo is", rollNo)


# function_1("Golu", 20, 10101)

# -----------, demonstration of *args:
def function_2(*argsjokes):  # here *args is way to take variable no of arguments, implicitly
    print(type(argsjokes))  # NOTE:
    if len(argsjokes) == 3:
        print("The name of the student is", argsjokes[0], "and age is", argsjokes[1], "and rollNo is", argsjokes[2])
        #  here we access the *args as a tuple
    else:
        print("The name of the student is", argsjokes[0], "and age is", argsjokes[1])


lis = ["Golu", 20, 2390]


# function_2(*lis)  # in *args we can pass only one value


# -----------, demonstration of **kargs:
def printMarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
        # here we access the **kargs as a dict


markList = {"name1": 100, "name2": 78, "name3": 90, "name4": 79, "name5": 98, "name6": 75, "name7": 90}
# printMarks(**markList)  # in **kargs we can pass a single or key-value(dict) pair


# -----------, combine demonstration with_master_function:
def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)


master("normal args", 23, 45, *lis, **markList)  # here we pass normal args , *args nd **kargs with together
