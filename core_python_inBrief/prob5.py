# def isPrime(n):
#     # n = 7
#     squareRoot = n ** 0.5
#     if squareRoot * 2 != n ** 2:
#         return True
#     else:
#         return False
#
#
# print(isPrime(4))

def isPrime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()


def f(i=2, h=3):
    return i * h


print(f(3))

t = (1,) + (1,)
t1 = t + t

print(t1)
