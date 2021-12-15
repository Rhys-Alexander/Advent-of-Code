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
                new_c = nc + inpt[y][x]
                if (x, y) in costs and costs[(x, y)] <= new_c:
                    continue
                costs[(x, y)] = new_c
                q.append((new_c, x, y))
        q.sort(reverse=True)


print(pathfind(day15()))
