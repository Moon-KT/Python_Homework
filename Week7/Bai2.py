def transpose_matrix(matrix):
    transposed =  [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed

row_n = int(input("Enter row: "))
column = int(input("Enter column: "))

matrix = []
for i in range(row_n):
    mini_matrix = []
    for j in range(column):
        m = int(input())
        mini_matrix.append(m)
    matrix.append(mini_matrix)

print(transpose_matrix(matrix))
