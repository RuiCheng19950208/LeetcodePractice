def rotate(matrix):
    n = len(matrix)
    for i in range(0, n - 1):
        for j in range(i, n - 1):
            if i <= ((n - 1) / 2) and j <= n - i - 2:
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]

    return matrix





matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix[0][0])
print(rotate(matrix))