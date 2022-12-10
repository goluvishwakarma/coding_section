# Date: 01-01-2021,
# Topic: Iterator, Iterable and Generators

"""

    1. Iterable(python_object) - in this object, __iter() and __getItem() is defined, which can gives a iterator.

    2. Iterator(python_object) - in this object, nextMethod() is defined, visit one element to another element nd so on.

    3. Iteration(python_object) - iterate any thing and fetching the next element to next and so on.

"""


# generators: it is iterator which is iterate from that only once, i.e we can generate the value once.
# which is capable to generate the operation
def gen(n):
    for j in range(n):
        yield j


# print(gen(1000000))  # it will give the address of the generator_object
# for i in gen(100):
#     print(i)

ob1 = gen(7)
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))

# iterable:
num = "code"  # string are iterable, but not int
iter1 = iter(num)
# for i in num:
#     print(i)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))  # here we will be  get an error
