# Date: 18.07.2021, @author...

# STRONG NUMBER,
# sum of the factorial of individual digit is equal to tha number.
# number[145]: 1! + 4! + 5! = 1 + [4 * 3 * 2 * 1] + [5 * 4 * 3 * 2 * 1]: 1 + 24 + 120: sum[145] == number[145]

def factorial(num):
    mul = 1

    for j in range(1, (num + 1)):
        mul *= j

    # return f"{num}! is: {mul}"
    return mul


def strong_number(number):
    to_string = str(number)  # convert into string
    add = 0  # to add the individual '!' , each_digit
    # mul = 1

    for i in to_string:  # "145", [1]in 1st iteration, [4]2nd iteration, ...
        # for j in range(1, (int(i) + 1)):  # [1st](1, 1+1: 1, 2), [2nd](1, 4 + 1: 1, 5), ...
        #     mul *= j  # [1st]mul(1): 1 * 1!(1): 1, [2nd]mul(1): 1 * 4!(24): 24, [3rd]mul(24): 24 * 5!(120): ...
        # so we have to mul value, after each iteration. otherwise it will store current value
        store = factorial(int(i))

        add += store  # add: 0 + 1: 1
        # add += mul
        # mul = 1  # here we update mul value, in each iteration

    # print(mul, " ", add)
    if number == add:
        print(f"{number}, is strong number")
        exit()

    return f"{number}, is NOT a strong number"


# print(factorial(0))
print(strong_number(40585))


def factor():
    num = 9
    # lst = []

    for i in range(1, (num + 1)):
        if num % i == 0:
            # lst.append(i)
            print(i)

    # return lst


factor()
