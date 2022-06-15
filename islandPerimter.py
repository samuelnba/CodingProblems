# Easy

grid = [[1,0]]
perimter = 0

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == 1:
            if column - 1 < 0:
                perimter += 1
            elif grid[row][column - 1] == 0:
                perimter += 1
            if column + 1 > len(grid[row]) - 1:
                perimter += 1
            elif grid[row][column + 1] == 0:
                perimter += 1
            if row - 1 < 0:
                perimter += 1
            elif grid[row - 1][column] == 0:
                perimter += 1
            if row + 1 > len(grid) - 1:
                perimter += 1
            elif grid[row + 1][column] == 0:
                perimter += 1

print(perimter)

# Better than 62.15% of people