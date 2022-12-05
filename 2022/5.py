stacks, moves = open("2022/5.txt").read().split("\n\n")
moves = [[int(x) for x in line.split() if x.isdigit()] for line in moves.splitlines()]
stacks = [
    [y for y in x if y != " "]
    for x in zip(*[[x for x in line[1::4]] for line in stacks.splitlines()[:-1]])
]

# Part 1
for move in moves:
    for i in range(move[0]):
        stacks[move[2] - 1].insert(0, stacks[move[1] - 1].pop(0))
print("".join(stack[0] for stack in stacks))
