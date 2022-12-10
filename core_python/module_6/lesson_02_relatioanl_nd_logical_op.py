# Date: 15-01-2021
# Topic: ------------ Relational And Logical Operator In Python

"""
    *. relational_operator:
    relational operator are used to evaluate condition inside the 'conditional_expression'.
        == ---- equals, NOTE ('=' is assignment operator, Not '==' )
        >= ---- greater than/equal to
        <= ---- less than/equal to
        != ---- not equal to    etc.

    *. logical_operator:
    logical operator operate on conditional statements .
    and ---- true if both operands are true else false.
    or ---- true if at least one operands is true else false.
    not ---- inverts true to false & false to true

"""
age = int(input("Enter your age: "))

if 18 < age < 30:
    print("you can work with us")
else:
    print("you cannot work with us")

