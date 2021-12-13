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
def printCode(inpt):
    coods, instrs = inpt
    for x_or_y, val in instrs:
        dim = 0 if x_or_y == "x" else 1
        for i, cood in enumerate(coods):
            if cood[dim] > val:
                coods[i][dim] = val - (cood[dim] - val)

    for y in range(max(y[1] for y in coods) + 1):
        line = ""
        for x in range(max(x[0] for x in coods) + 1):
            dot = "\u2588" if [x, y] in coods else " "
            line += dot
        print(line)


printCode(day13())
