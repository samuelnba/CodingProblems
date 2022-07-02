def checkXMatrix(grid):
    length = len(grid)
    for i in range(length):
        if grid[i][i] == 0:
            return False
        grid[i][i] = -1
    for i in range(length):
        if grid[i][-i-1] == 0:
            return False
        grid[i][-i-1] = -1
    for i in grid:
        for j in i:
            if j != 0 and j != -1:
                return False
    return True

print(checkXMatrix([[5,7,0],[0,3,1],[0,5,0]]))