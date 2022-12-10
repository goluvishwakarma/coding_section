# here in this we find the time execution of a python_program:
from time import time


def func1(a, b):
    # By anjali
    return a + b


def func2(a, b):
    # By CodeWithGolu
    num1 = a
    num2 = b
    if a > b and a != 3:
        pass
    sum([4, 3])
    return a + b


# here we find the individual execution_time of each function:
# if __name__ == '__main__':
#     init = time()  # here init is initializing time(),
#     for i in range(0, 100000):
#         func1(1, 5)
#     print("Anjali's Execution Time: ", time() - init)
#
#     init = time()
#     for i in range(0, 100000):
#         func2(4, 5)
#     print("CodeWithGolu's Execution Time: ", time() - init)


# here we find the overall execution_time the program:

if __name__ == '__main__':
    init = time()

    for i in range(0, 100000):
        func1(1, 1)

    for j in range(0, 100000):
        func2(34, 56)

    print("Overall Execution Time is: ", time() - init)
