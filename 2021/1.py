# Part 1
def getNumTimesIncreased(inpt):
    increased = 0
    for i, x in enumerate(inpt[1:]):
        if x > inpt[i]:
            increased += 1

    return increased


# Part 2
def getNumTimesBandIncreased(inpt):
    increased = 0
    for i, x in enumerate(inpt[1:-2]):

        if (inpt[1:][i] + inpt[1:][i + 1] + inpt[1:][i + 2]) > (
            inpt[i] + inpt[i + 1] + inpt[i + 2]
        ):
            increased += 1

    return increased
