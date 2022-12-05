from copy import deepcopy

stacks, moves = open("2022/5.txt").read().split("\n\n")
moves = [[int(x) for x in line.split() if x.isdigit()] for line in moves.splitlines()]
og_stacks = [
    [y for y in x if y != " "]
    for x in zip(*[[x for x in line[1::4]] for line in stacks.splitlines()[:-1]])
]


def part1():
    for i in range(move[0]):
        stacks[move[2] - 1].insert(0, stacks[move[1] - 1].pop(0))


def part2():
    stacks[move[1] - 1], stacks[move[2] - 1] = (
        stacks[move[1] - 1][move[0] :],
        stacks[move[1] - 1][0 : move[0]] + stacks[move[2] - 1],
    )


for part in (part1, part2):
    stacks = deepcopy(og_stacks)
    for move in moves:
        part()
    print("".join(stack[0] for stack in stacks))
