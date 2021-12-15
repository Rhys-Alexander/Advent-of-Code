from inpt import day15


def coodInRange(cood, inpt):
    return cood[0] in range(len(inpt)) and cood[1] in range(len(inpt[0]))


def pathfind(inpt):
    q = [(0, 0, 0)]
    costs = dict()
    while True:
        nc, nx, ny = q.pop()
        if nx == len(inpt) - 1 and ny == len(inpt[0]) - 1:
            return nc
        for x, y in [(nx + a, ny + b) for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0))]:
            if coodInRange((x, y), inpt):
                new_c = nc + inpt[x][y]
                if (x, y) in costs and costs[(x, y)] <= new_c:
                    continue
                costs[(x, y)] = new_c
                q.append((new_c, x, y))
        q.sort(reverse=True)


def enlarge(inpt):
    blocks = [inpt]
    while len(blocks) != 9:
        block = []
        for line in blocks[-1]:
            new_line = []
            for x in line:
                val = 1 if (x + 1) > 9 else (x + 1)
                new_line.append(val)
            block.append(new_line)
        blocks.append(block)

    enlarged = []
    for i in range(5):
        row = blocks[i]
        for j in range(1, 5):
            for k, line in enumerate(blocks[i + j]):
                row[k].extend(line)
        enlarged.extend(row)
    return enlarged


# Part 1
print(pathfind(day15()))


# Part 2
print(pathfind(enlarge(day15())))
