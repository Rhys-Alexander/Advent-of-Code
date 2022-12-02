# Part 1
def getMaxCalories():
    return max(
        sum(int(x) for x in elf.split("\n"))
        for elf in open("2022/1.txt").read().split("\n\n")
    )


print(getMaxCalories())


# Part 2
def getMax3Calories():
    return sum(
        sorted(
            sum(int(x) for x in elf.split("\n"))
            for elf in open("2022/1.txt").read().split("\n\n")
        )[-3:]
    )


print(getMax3Calories())
