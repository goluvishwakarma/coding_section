# date: 27.11.20, Author: @golu_vishwakarma,
import math  # here we import math module_1

# This is 'a single line' comment

print("\"Hello, World\"")  # this is our 1st program in python
# here '#' is a single line comment

''' 
    here print is built-in function, 
    "" -- is called double quote whatever we write within the double quote("") will be print as it is. 
'''
"""  
    This ia multiline comment,
    
    Python is a Object_Oriented programming language.
    Programming language: is medium to interact with computer(machine).
    
    Just like when we communicate with others we used a specific languages.
    language may be hindi, english, bengali, tamil, chinese nd many more like local_languages etc.

"""

# here multiline comment is started from """ ND closing """, NOTE: quote may be single('),
#  or double(") both are recognised by multiline comment.

# here we are going to take input from the user, using input() function, which is a 'in-built function'.
# age = int(input("Enter your age: "))
age = 10  # hard_coded
if age < 18:
    print("You are not eligible to vote!!!")
    # indentation, space before the print statement is called indentation

else:
    print("You are eligible to vote\n")  # here '\n' is escape sequence, it takes the cursor in new line

# here we called '(' opening parenthesis ND,  ')' called closing parenthesis

print("greatest common divisor of these number(23, 11):", math.gcd(23, 11))
print("square root of the number(25): ", math.sqrt(25))
print("another way to evaluate the square_root is: ", (49 ** 0.5))  # NOTE,
print("square of a number is: ", (3 ** 2))  # output: 9, here '**' is exponentiation_operator.

# variable in python,
# variables: are containers, which store some values(data -- in a single word 'information').
# Here we can give any name to variable

var1 = 3  # integer
var2 = "coding"  # string
var3 = 3.09  # floating

print(var1 + 23)
print(var1 / var3)  # here / gives the quotient
print(var1 % var3)  # % gives the remainder
print(var1 - var3)

# quick Quiz: Try these operators,

# 1. ** exponentiation operator, it will raise the power, Ex: 2 ** 3 = 8
# 2. // Floor division_operator or integer_division, it will return integer
# 3. % Modulo operator -- it will give remainder
# NOTE: We can also say, // -- Integer Division

# python value = 34   # wrong syntax, it will throw an error
# because, constructing the variable whitespace is not allowed,(here, whitespace bet. python nd value)
# it violets the creating_variable rules.


# ---- :RULES FOR CREATING VARIABLE: ----, 'REMEMBER IN MIND WHENEVER WE GOING TO CREATE VARIABLE '

# 1. variable name should start with a letter or an underscore(_).
# 2. variable cannot start with a number. Ex: 1var is invalid variable
# 3. It can only contain alpha numeric character.(0, 1, ... 9 ND a-z or A-Z
# 4. variable name are case sensitive. Ex: Var and var both are different variables.


print(type(var1))
# here type() is in-built function which tells the type(data_type) of variable

print(type(var2))
print(type(var3))

a = 31  # is a integer
b = "31"  # is a string

# a = 33
# here we can also store another value in existing variable ND also change data_type

b = int(b)  # type casting
# type_casting: convert one data_type to another data_type.
print(type(b))
print(b + 4)

c = 23.34
print(c + 4)

d = 23
d = str(d)  # here we convert integer to string
e = "hii"
print(d + e)

h = int("22")
print("\ntype of the variable(h): ", type(h))

# Quick Quiz:
# create each variable for integer, float ND string,
# convert int to string and float, string to int and float ND float to string and int.

# type_casting int to float ND string
i = 2  # create a integer var
f = float(i)
print("after type_casting the variable type is: ", type(f), f)
s = str(i)
print("after type_casting the variable type is: ", type(s), s, "\n")

# type_casting float to int ND string
f1 = 3.5  # create a float var
i1 = int(f1)
print("after type_casting the variable type is: ", type(i1), i1)
s1 = str(f1)
print("after type_casting the variable type is: ", type(s1), s1, "\n")

# type_casting string to int ND float
s2 = "5"
i2 = int(s2)
print("after type_casting the variable type is: ", type(i2), i2)
f2 = float(s2)
print("after type_casting the variable type is: ", type(f2), f2)

name = "LEARN_PYTHON " \
       "IN_SMART_WAY"  # note: here '\' refers to continue the statement in single_line

print(name)
name1 = 'learn_python' \
        '_in_smart_way'
print(name1)  # NOTE: here, '\' means continue the line or statement

name2 = """LEARN_PYTHON
       _IN_ONE_VIDEO"""
print(name2)

name3 = '''learn_python
       _in_one_video'''  # NOTE: here we create a multiline_string ND also design the string
print(name3, "\n")

# -------:NOTE:--------

# SLICING: is the process where we can access the particular index_element from the entire string.

print(name[0])  # here we done slicing
print(name[3])
print(name[2:5])  # here index starts from 2 ND go up to 5 - p.jpg = 4th_index, NOTE

st = "slicingStriping"
print(st)
print(st.strip())  # Here strip() function, will remove the whitespaces
print("length of the string is: ", len(st))  # it will give length of the string

var = st.lower()  # it will convert the string into lower_case
print(var)

var = st.upper()  # it will convert the string into upper_case
print(var)

# --------- Date: 29.11.20 -----------

print("length of the string: ", len(st))
# here len() is also in-built function, gives the length of the function.

var = st.replace('Str', 'aa')  # here we replace str with aa
print(var)

var_a = "shubham, rohan, mode, ram"
print("before replacing the comma, string is: ", var_a)
var = var_a.replace(",", '')  # we replace the comma(,) with blank_space
print("after replacing the string with blank_space is: ", var)

st1 = "This is "
name1 = "shubham"
name2 = "sunder"
st2 = "python"
print(st1 + st2)  # Here we concatenate the string

# create a template
temp = "This is a {0} and he is a good boy named {1}".format(name1, name2)  # {} is place_holder
print(temp)
temp = "This is a {1} and he is a good boy named {0}".format(name1, name2)
print(temp)

# f string
temp = f"this is a {name1} and he is a good boy {name2}"  # introduced in python_3
print(temp)

'''
    ---------:Python Collection:---------
    
    1. List
    2. Tuple
    3. Set
    4. Dictionary

'''
# >>>>>>> :List: <<<<<<<
lst = [43, 3, 2, 45, 1, 34]  # list are ordered ND changeable(mutable)
# var = lst[3]
# var = type(lst)
# print(var)
#
# var = len(lst)  # it will give the length of the list
# print("list_length: ", var)
#
# lst[3] = 22  # it will replace the element at that index_position by given specified element.
# lst.append(100)  # here append() function will add the an element at the end of the list.
# lst.insert(p.jpg, 200)  # it will add the element at that particular index_pos.
#
# lst.remove(200)  # it will remove the specified element
# lst.pop()  # it will remove the automatically an element from the end of the list.

# del lst[3]  # it will delete the element from the specified position(index_position).
# del lst  # it will delete the entire lst
#
# var = lst
# print(var)  # it will throw error because we deleted the list

# lst.clear()
# var = lst
# print(var)  # it will give empty list

# lst.reverse()
# var = lst
# print(var)

# >>>>>>>>tuple: are unchangeable(immutable). <<<<<<<<<<
tup = ("harry", "rohan", "shubham")
var = tup
print(var)
var = type(tup)
# tup[0] = "suraj" it will throw error because tuple are unchangeable(un-mutable)
print(var)

var = list(tup)  # here we done type_casting, so now, our tuple is converted into list
var[0] = "suraj"  # now, it is valid
print(var)

# >>>>>>>>>> set: sets is a collection of well defined objects. <<<<<<<<<<<<
Set = {2, 1, 4, 5, 7, 4, 5, 3, 3, 9}
Set.add(234)  # it will add the element at end of the set.

Set.update([11, 12, 45, 13, 18, 15])  # here we give a list as an argument
print("length of the set: ", len(Set))

# Set.remove(235)  # it remove the specified element if the element present else throw_error
Set.discard(234)  # it will discard the element it the element present otherwise leave it,
# does n't throw error

print(Set)  # sets does not repeats element.
# here we can use .pop(), .clear(), del, and, intersection. union


# >>>>>>>> dictionary: <<<<<<<<<

demoDict = {
    "Name": "shubham",
    "Class": "5th",
    "Marks": "35",
    "SchoolName": "SVM"

}

print(demoDict["Marks"])
demoDict["Marks"] = 94  # here we update the Marks
# demoDict.pop("Marks")  # here we popup the marks from the dictionary
print(demoDict)  # here we can use del, pop, clear, update

# --------------Conditional Statement:----------------

# age = input("Enter Your age: ")
# # NOTE: whatever input() capture, that's will be string
# # to avoid the problem we have to do type_casting
# age = int(age)
# # print(type(age)) # now it will be show int_type
#
# if age > 18:
#     print("You can drive a car")
#
# elif age == 18:
#     print("You are an awesome teen")
#
# else:
#     print("You cannot drive")

# -------------- loop(iterative statement: --------------

# Scenario: We have to print number between 1 - 1000
for i in range(0, 10):
    print(i, end=" ")  # here end, stop the cursor to goes in new line, i.e: it prints the data in a single line
# here we add + p.jpg because, we have print p.jpg - 100, so the 1st element will be p.jpg,
# otherwise it will be start print from 0.
print("\n")

li = [1, 432, "this"]
for item in li:
    print(item)  # here we iterate the each item for list

# Quick Quiz: Use for loop to iterate dictionary, set and tuples
# --------------------------------------------------------
# Question: 1.
# for key_v in demoDict:
#     print(key_v)  # here we iterate the dictionary key_values

# Question: 2.
for ele in Set:
    print(ele, end=" ")  # iterate the each element of the set
print("\n")

# Question: 3.
for item in tup:
    print(item, end=" ")  # here we iterate the each data of tuple
# --------------------------------------------------------
print("\n")

# _________ :while loop: __________
# Syntax:

# initializing_variable
# while condition:
#    Statement_1
#    Statement_2...
#    update_variable

i = 0  # here we initialize the variable

while i < 10:  # here condition is checking
    i = i + 1  # here we update the value of i each time after the condition_checking
    if i == 5:
        # break  # Here break statement will terminate loop when i = 5. i.e: stop(break) the execution.
        continue  # it will skip the 'that value'
    print(i + 1, end=" ")  # the print statement will be execute, until the condition is true


# --------- Date: 06.12.20 ---------

# FUNCTION: A BLOCK OF CODE WHICH PERFORM CERTAIN TASK.
def greet():  # function definition
    print("\nGood morning ma'am")
    print("How are you,")


greet()  # function calling


# Here we create a function(add()) which return sum of two number
def add(x, y):
    r = x + y
    return r  # it returning sum of these number


s = add(34, 45)
print("summation of these number: ", s)

# in format_specifier way , we can also write
# print(f"summation of {34} and {45}: ", add(34, 45))  # we can also write, in this way
# we can also change the order, note - the result will be also change


# ----------- :OOPs -- Object Oriented Programming: [A Smart Code Re-usability] ------------

# Object Oriented programming is a way of programing.
# Class: is a template.


class Employee:  # here we create a class name Employee
    # pass  # is a keyword, which is used when we want to keep empty, our class.
    def __init__(self, g_name, g_salary):  # constructor
        self.name = g_name
        self.salary = g_salary


harry = Employee("harry", "7.6lpa")  # here we create object(harry) of class Employee and pass two argument
print(harry.name)
print(harry.salary)


# ------- Date: 09.12.20

class Employee:  # parent class
    increment = 1.5  # class variable
    no_of_employee = 0

    def __init__(self, f_name, l_name, salary):  # constructor - automatic fill up
        self.f_name = f_name  # class instance variable
        self.l_name = l_name
        self.salary = salary
        # self.increment = 2.0
        Employee.no_of_employee += 1

    def increase(self):  # here we create a function
        print("\"code in increase() function\"")
        self.salary = self.salary * self.increment  # 1st it's search in instance variable, then go to class_var
        # self.salary = self.salary * Employee.increment  # it will direct access the class variable without searching
        # in instance variable

    @classmethod  # is a class_method, @ is a decorator
    def change_increment(cls, amount):  # it's take the class as an argument, ND update the value
        cls.increment = amount
        """
            if we want to run a function which doesn't belongs to instance variable,
            but, belongs to direct class variable. then we use class_method in which,
            we pass the class as an argument.
            
            Here we want to change the one variable of class, so we created a class_method.
            it doesn't take the object as an argument.
            
            NOTE: When we want to access the class variable only, then we use class_method.
            
            
        """

    # Class_Method As Alternative Constructor
    @classmethod
    def from_str(cls, emp_string):
        f_name, l_name, salary = emp_string.split("-")
        return cls(f_name, l_name, salary)

    # static method: we use, when we don't want to access the class ND instance variables.
    @staticmethod
    def is_open(day):  # also called independent_function
        if day == "sunday":
            return False
        else:
            return True


# print(Employee.no_of_employee)
# rohan = Employee("rohan", "rambo", 30)  # here we create a object name rohan of class Employee
# lav = Employee("lav", "son", 40)  # here we create another object name lav of class Employee
# print(Employee.no_of_employee)

# rohan.f_name = "rohan"
# rohan.l_name = "sharma"
# rohan.salary = "3.2lpa"
#
# lav.f_name = "lav"
# lav.l_name = "mishra"
# lav.salary = "3.7lpa"

# print(rohan, lav)  # it will give the address of the objects
# print(rohan.f_name, lav.f_name)
# print(rohan.__dict__)  # it will show all the variable of instance variable,

# print(rohan.salary)  # it will show pre-increment salary

# lav.increase()
# print(lav.salary)
#
# rohan.increment = 9
# print(rohan.__dict__)
# # print(Employee.__dict__)  # it will give all the variables of the Employee class


# rohan = Employee("rohan", "rambo", 30000)  # here we create a object name rohan of class Employee
# lav = Employee("lav", "son", 40000)  # here we create another object name lav of class Employee
# kiran = Employee.from_str("kiran-singh-25000")
#
# print(kiran.l_name)

# print("rohan's current_salary: ", rohan.salary)
# Employee.change_increment(9)
# rohan.increase()  # it's incremented the salary
# print("rohan's upgraded_salary: ", rohan.salary)

# shubham = Employee("shubham", "sharma", 780000)
# print(Employee.is_open("sunday"))  # here we can call this method without object and also by creating_object.
# print(Employee.is_open("monday"))  # here we call the method bt using class_name(Employee).function_name(is_open)
# print(shubham.is_open("tuesday"))  # here we calling the method by using instance

# --------- :INHERITANCE: Inherit the property of base_class. --------

# class Programmer(Employee):  # child class
#     def __init__(self, f_name, l_name, salary, code_lang, exp):
#         super().__init__(f_name, l_name, salary)
#         self.code_lang = code_lang
#         self.exe = exp
#
#     def increase(self):
#         # print("\"code in child_class increase() function\"")
#         self.salary = int(self.salary * (self.increment + 0.2))
#         return self.salary
#
#
# rohan = Programmer("rohan", "sharma", 99000, "python", "5 yrs")
# print(rohan.code_lang)
# print(rohan.increase())
# # print(rohan.salary)
# # print(rohan.exp)
# # print(help(Programmer))  # it will give the whole class description
# # help(Programmer)


# ------- Dun_der/Magic Method:


rohan = Employee("rohan", "sharma", 99000)
lav = Employee("lav", "das", 95000)
print(rohan.salary)

