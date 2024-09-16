def flipAndInvertImage(A):
    return [list(map(lambda x, y: x ^ y, row[::-1], len(row) * [1])) for row in A]

A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(A))