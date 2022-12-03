import string

PRIORITY = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}

# Part 1
def getPrioritySum():
    return sum(
        PRIORITY[
            set(line[: len(line) // 2]).intersection(set(line[len(line) // 2 :])).pop()
        ]
        for line in open("2022/3.txt")
    )


print(getPrioritySum())
