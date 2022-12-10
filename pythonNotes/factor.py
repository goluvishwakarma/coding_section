# Date: 19.07.2022, @author...

# factor: a number that divides another number, i.e. with no remainder. let, 6: 1 2 3, 18: 1 2 3 6 9

def factor(num):
    count = 0
    lst = []

    for i in range(1, (num + 1)):
        if num % i == 0:
            for j in range(1, (i + 1)):
                if i % j == 0:
                    count += 1
                    lst.append(i)
            # print(i)

    return lst


print(factor(18))
