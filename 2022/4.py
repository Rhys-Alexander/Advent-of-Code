from re import split as re_split

lines = [[int(a) for a in re_split(",|-", line.strip())] for line in open("2022/4.txt")]

# Part 1
def getEnvelopingLines():
    return sum(
        1
        for l in lines
        if (l[0] >= l[2] and l[1] <= l[3]) or (l[2] >= l[0] and l[3] <= l[1])
    )


print(getEnvelopingLines())
