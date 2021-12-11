from inpt import day11


# Part 1
def sumFlashes(inpt, steps):
    for line in inpt:
        line.append(0)
    inpt.insert(len(inpt), [0 for _ in inpt[0]])

    flashes = 0
    for _ in range(steps):
        for line_i, line in enumerate(inpt):
            inpt[line_i] = [x + 1 for x in line]

        flashed = []
        while len([x for line in inpt[:-1] for x in line[:-1] if x > 9]) != len(
            flashed
        ):
            for line_i, line in enumerate(inpt[:-1]):
                for num_i, num in enumerate(line[:-1]):
                    if num > 9 and (line_i, num_i) not in flashed:
                        flashed.append((line_i, num_i))
                        for i in (-1, 0, 1):
                            for n in (-1, 0, 1):
                                inpt[line_i + i][num_i + n] += 1

        for line_i, num_i in flashed:
            inpt[line_i][num_i] = 0
            flashes += 1

    return flashes


print(sumFlashes(day11(), 100))


# Part 2
def getSynchronizedStep(inpt):
    for line in inpt:
        line.append(0)
    inpt.insert(len(inpt), [0 for _ in inpt[0]])

    step = 0
    while sum(x for line in inpt[:-1] for x in line[:-1]) != 0:
        step += 1
        for line_i, line in enumerate(inpt):
            inpt[line_i] = [x + 1 for x in line]

        flashed = []
        while len([x for line in inpt[:-1] for x in line[:-1] if x > 9]) != len(
            flashed
        ):
            for line_i, line in enumerate(inpt[:-1]):
                for num_i, num in enumerate(line[:-1]):
                    if num > 9 and (line_i, num_i) not in flashed:
                        flashed.append((line_i, num_i))
                        for i in (-1, 0, 1):
                            for n in (-1, 0, 1):
                                inpt[line_i + i][num_i + n] += 1

        for line_i, num_i in flashed:
            inpt[line_i][num_i] = 0

    return step


print(getSynchronizedStep(day11()))
