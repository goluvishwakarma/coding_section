import cmath
import math
import sys

"""
    in this program we have to find square_root of the quadratic equation,
    quadratic_equation: ax^2 + bx + c = 0.
"""

# ALGORITHM: is a step by step process to solve a problem.

# step-p.jpg: take the coefficients of equ. through user_input .
# step-2: find discriminant of the equation(d = b^2 - 4ac).
# step-4: find root_1(for_+ve term) and root_2(for_-ve term):
# step-3: check, if(d == 0):
#                    print: roots are real and same, root_1, root-2.
#                elif(d > 0):
#                    print: roots are real and distinct, root_1, root_2.
#                else:
#                    print: roots are imaginary, root_1, root_2.
# step-4: stop.

var = sys.version
print("system_version: ", var)


def real_nd_sameRoot(c1, c2, d):
    root_1 = (-c2 + math.sqrt(d)) / (2 * c1)
    root_2 = (-c2 - math.sqrt(d)) / (2 * c1)

    return root_1, root_2


def real_nd_distinctRoot(c1, c2, d):  # (to check the block of code: x + 5x + 4 = 0)
    root_1 = (-c2 + math.sqrt(d)) / (2 * c1)
    root_2 = (-c2 - math.sqrt(d)) / (2 * c1)

    return root_1, root_2


def imaginaryRoot(c1, c2, d):
    # print("roots of the equation are imaginary:\n")
    root_1 = (-c2) / (2 * c1) + cmath.sqrt(d) / (2 * a)
    root_2 = (-c2) / (2 * c1) - cmath.sqrt(d) / (2 * a)

    return root_1, root_2


a = float(input("Enter the 1st coefficients: "))
b = float(input("Enter the 2nd coefficient: "))
c = float(input("Enter the 3rd coefficient: "))
print(f"entered_equation is: ({a}x^2) + ({b}x) + ({c}) = 0")

dis = ((b ** 2) - (4 * a * c))
print("discriminant of the equation: ", dis)

if dis == 0:
    print("roots of the equation are real and same: ", "\n", real_nd_sameRoot(a, b, dis))

elif dis > 0:
    print("roots of the equation are real and distinct: ", "\n", real_nd_distinctRoot(a, b, dis))

else:
    print("roots of the equation are imaginary: ", "\n", imaginaryRoot(a, b, dis))
    a = input()
