from inpt import day2


# Part 1
def sumPosition(inpt):
    direction = {"up": -1, "down": 1}
    horizontal = sum(y for x, y in inpt if x == "forward")
    depth = sum(y * direction[x] for x, y in inpt if x != "forward")
    return horizontal * depth


print(sumPosition(day2()))


# Part 2
def sumAimedPosition(inpt):
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


print(sumAimedPosition(day2()))
