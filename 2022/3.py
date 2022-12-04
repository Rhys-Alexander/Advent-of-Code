from string import ascii_letters

PRIORITY = {letter: i + 1 for i, letter in enumerate(ascii_letters)}

# Part 1
print(
    sum(
        PRIORITY[
            set(line[: len(line) // 2]).intersection(set(line[len(line) // 2 :])).pop()
        ]
        for line in open("2022/3.txt")
    )
)

# Part 2
lineSets = [set(line.strip()) for line in open("2022/3.txt")]
triples = tuple(zip(lineSets[::3], lineSets[1::3], lineSets[2::3]))
print(
    sum(PRIORITY[group[0].intersection(group[1], group[2]).pop()] for group in triples)
)
