from copy import deepcopy

stacks, moves = open("2022/5.txt").read().split("\n\n")
moves = [[int(x) for x in line.split() if x.isdigit()] for line in moves.splitlines()]
og_stacks = [
    [y for y in x if y != " "]
    for x in zip(*[[x for x in line[1::4]] for line in stacks.splitlines()[:-1]])
]
# Part 1
stacks = deepcopy(og_stacks)
for move in moves:
    for i in range(move[0]):
        stacks[move[2] - 1].insert(0, stacks[move[1] - 1].pop(0))
print("".join(stack[0] for stack in stacks))

# Part 2
stacks = deepcopy(og_stacks)
for move in moves:
    a, b, c = move
    stacks[b - 1], stacks[c - 1] = (
        stacks[b - 1][a:],
        stacks[b - 1][0:a] + stacks[c - 1],
    )
print("".join(stack[0] for stack in stacks))
