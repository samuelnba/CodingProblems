def diagonalsum(mat):
    length = len(mat)
    summ = 0
    for i in range(length):
        summ += mat[i][i]
    for i in range(length):
        summ += mat[i][-(i+1)]
    if length % 2 != 0:
        summ -= mat[int(length/2)][int(length/2)]
    return summ

print(diagonalsum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))