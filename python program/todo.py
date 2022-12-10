d = {"one": "two", "three": "one", "two": "three"}
v = d["three"]

for k in range(len(d)):
    v = d[v]

print(v)


# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")
def f(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(f(f(2)))
l = [1, 2]
for i in range(2):
    l.insert(-1, l[i])

print(l)
d = {'1': (1, 2), '2': (2, 1)}

for i in d.keys():
    print(d[i][1], end="")

t = (1, 2, 4, 8)
t = t[-2:-1]
t = t[-1]
print(t)
print()
print(2 % 3)


def f(i=2, j=3):
    return i * j


print(f(j=2))

print(1 // 2)

l1 = [1, 2, 3]
l2 = l1
print(l2)


def f1(a):
    return None


def f2(a):
    return f1(a) * f1(a)


print(f2(2))
