from inpt import day1

# Part 1
def getMaxCalories(inpt):
    return max(sum(int(x) for x in elf.split("\n")) for elf in inpt.split("\n\n"))


print(getMaxCalories(day1()))


# Part 2
def getMax3Calories(inpt):
    return sum(
        sorted(sum(int(x) for x in elf.split("\n")) for elf in inpt.split("\n\n"))[-3:]
    )


print(getMax3Calories(day1()))
