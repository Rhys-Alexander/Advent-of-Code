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


# Part 2
def getPrioritySumFromTriples():
    lineSets = [set(line.strip()) for line in open("2022/3.txt")]
    triples = tuple(zip(lineSets[::3], lineSets[1::3], lineSets[2::3]))
    return sum(
        PRIORITY[group[0].intersection(group[1], group[2]).pop()] for group in triples
    )


print(getPrioritySumFromTriples())
