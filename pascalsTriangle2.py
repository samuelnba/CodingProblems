def getrow(rowIndex):
    triangle = [[1]]
    for i in range(rowIndex):
        triangle.append([])
        for j in range(len(triangle[i]) + 1):
            triangle[i + 1].append(0)
        for j in range(len(triangle[i+1])):
            if j-1 < 0:
                triangle[i+1][j] = triangle[i][j]
            elif j == len(triangle[i+1]) - 1:
                triangle[i+1][j] = triangle[i][j-1]
            else:
                triangle[i+1][j] = triangle[i][j-1] + triangle[i][j]
    return triangle

print(getrow(4))

# Better than 13% of people