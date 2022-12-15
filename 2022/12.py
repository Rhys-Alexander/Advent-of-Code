import collections

grid = [
    [ord(char) for char in line.strip()] for line in open("2022/12.txt").readlines()
]
start, goal = None, None
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == 83:
            grid[y][x] = 97
            startCood = (x, y)
        if col == 69:
            grid[y][x] = 122
            goal = (x, y)
        if start and goal:
            break
# print(start, goal, grid)


def bfs(start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            return len(path) - 1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                0 <= x2 < len(grid[1])
                and 0 <= y2 < len(grid)
                and (grid[y2][x2] <= grid[y][x] + 1)
                and (x2, y2) not in seen
            ):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


# Part 1
print(bfs(startCood))

# Part 2
print(
    min(
        filter(
            lambda item: item is not None,
            [
                bfs((x, y))
                for y, row in enumerate(grid)
                for x, col in enumerate(row)
                if col == 97
            ],
        )
    )
)
