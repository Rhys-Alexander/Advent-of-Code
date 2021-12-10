from inpt import day1


# Part 1
def getNumTimesIncreased(inpt):
    return sum(1 for x, y in zip(inpt[1:], inpt) if x > y)


print(getNumTimesIncreased(day1()))


# Part 2
def getNumTimesBandIncreased(inpt):
    bands = [sum([inpt[i], inpt[i + 1], inpt[i + 2]]) for i in range(len(inpt) - 2)]
    return sum(1 for x, y in zip(bands[1:], bands) if x > y)


print(getNumTimesBandIncreased(day1()))
