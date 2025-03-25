n = 3  
m = 4  

matrix = [
    [1, 2, 3, 4],
    [5, 6, 9, 8],
    [7, 9, 3, 2]
]

max_val = matrix[0][0]
row_idx = 0
col_idx = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            row_idx = i
            col_idx = j

print(row_idx, col_idx)

# Вхідні дані:
# n = 3
# m = 4
# 1 2 3 4
# 5 6 9 8
# 7 9 3 2
#
# Вихідні дані:
# 1 2  (бо перша "9" на позиції 1 рядок, 2 стовпець)
