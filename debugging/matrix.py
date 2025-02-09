sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy()) # makes a shallow copy
    # or matrix.append(sub_list[:])
    # or matrix.append(list(sub_list))


matrix[0][0] = "X"
matrix[1][1] = "O"
matrix[2][2] = "X"
print(matrix)

print(id(matrix[0]))
print(id(matrix[1]))
print(id(matrix[2]))
