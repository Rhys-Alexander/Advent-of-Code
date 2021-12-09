# Part 1
def getSumOfPosition(inpt):
    horizontal = 0
    depth = 0
    for x, y in inpt:
        if x == "forward":
            horizontal += y
        elif x == "down":
            depth += y
        else:
            depth -= y

    return horizontal * depth


# Part 2
def getAimedPosition(inpt):
    horizontal = 0
    depth = 0
    aim = 0
    for x, y in inpt:
        if x == "forward":
            horizontal += y
            depth += y * aim
        elif x == "down":
            aim += y
        else:
            aim -= y

    return horizontal * depth
