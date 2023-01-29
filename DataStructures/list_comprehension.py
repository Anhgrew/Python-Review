# from math import pi
# a = [x**2 for x in range(10)]
# print(a)

# print(list(map(lambda x: x*x, range(10))))
# tmp = []
# print([tmp.append((x, y)) for x in [1, 2, 3] for y in [1, 2, 3] if x > y])

# print(tmp)

# print([str(round(pi, i)) for i in range(10)])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(matrix)
# transpose_matrix = [ [x[i] for x in matrix] for i in range(len(matrix))]


# print([ [ x[i] for x in matrix] for i in range(len(matrix[0]))])

# print([[ arr[i] for arr in matrix if arr[i] %2 == 0] for i in range(3) if i == 0 ])