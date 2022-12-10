# 22/02/2021, @_author

# topic: matrix addition


# def matrix(A):
#     o = []
#     for a in range(len(A)):
#         row = []
#         for b in range(len(A[0])):
#             row.append(A[a][b])
#         o.append(row)
#     return o
#
#
# def sum(A, B):
#     output = []
#     for i in range(len(A)):
#         row = []
#         for j in range(len(A[0])):
#             row.append(A[i][j] + B[i][j])
#         output.append(row)
#     return output
#
#
# A = [[1, 2, 3],
#       [4, 5, 6],
#       [0, 8, 7]]
#
# B = [[3, 1, 2],
#       [4, 1, -3],
#       [2, 0, -1]]
#
# print("Matrix A")
# print(matrix(A))
#
# print("Matrix B")
# print(matrix(B))
#
# print(sum(A, B))


def input_sum(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


def input_matrix(m, n):
    out = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]: "))
            row.append(inp)
        out.append(row)
    return out


m = int(input("Enter the value of row m: \n"))
n = int(input("Enter the value of column n: \n"))

print("Enter matrix A: ")
A = input_matrix(m, n)
print(A)

print("Enter matrix B: ")
B = input_matrix(m, n)
print(B)

s = input_sum(A, B)
print("Sum: ", s)
