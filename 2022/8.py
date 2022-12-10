grid = [[int(tree) for tree in line.strip()] for line in open("2022/8.txt").readlines()]

# Part 1
visibleTrees = len(grid[0]) * 2 + len(grid) * 2 - 4
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        height = grid[i][j]
        if (
            max(grid[i][:j]) < height
            or max(grid[i][j + 1 :]) < height
            or max([row[j] for row in grid[:i]]) < height
            or max([row[j] for row in grid[i + 1 :]]) < height
        ):
            visibleTrees += 1

print(visibleTrees)
