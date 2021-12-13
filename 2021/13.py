from inpt import day13


# Part 1
def sumFoldedDots(inpt, folds):
    coods, instrs = inpt
    for fold in range(folds):
        x_or_y, val = instrs[fold]
        dim = 0 if x_or_y == "x" else 1
        for i, cood in enumerate(coods):
            if cood[dim] > val:
                coods[i][dim] = val - (cood[dim] - val)
    return len(set(tuple(cood) for cood in coods))


print(sumFoldedDots(day13(), 1))


# Part 2
def getCode(inpt):
    coods, instrs = inpt
    for x_or_y, val in instrs:
        dim = 0 if x_or_y == "x" else 1
        for i, cood in enumerate(coods):
            if cood[dim] > val:
                coods[i][dim] = val - (cood[dim] - val)

    grid = [
        [[x, y] for x in range(max(x[0] for x in coods) + 1)]
        for y in range(max(y[1] for y in coods) + 1)
    ]
    for line_i, line in enumerate(grid):
        for cood_i, cood in enumerate(line):
            if cood in coods:
                grid[line_i][cood_i] = "#"
            else:
                grid[line_i][cood_i] = " "
    for line in grid:
        print(line)
    return len(set(tuple(cood) for cood in coods))


print(getCode(day13()))
