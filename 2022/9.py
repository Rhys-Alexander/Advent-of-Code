instrs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def getTailPositions(k):
    positions = set()
    for line in open("2022/9.txt"):
        instr, val = line.strip().split()
        for i in range(int(val)):
            k[0][0] += instrs[instr][0]
            k[0][1] += instrs[instr][1]
            for i in range(1, len(k)):
                a, b = k[i - 1][0] - k[i][0], k[i - 1][1] - k[i][1]
                if abs(a) > 1 or abs(b) > 1:
                    if a == 0 or b == 0:
                        k[i][1] += b // 2
                        k[i][0] += a // 2
                    else:
                        k[i][0] += 1 if a > 0 else -1
                        k[i][1] += 1 if b > 0 else -1
            positions.add(tuple(k[-1]))

    return len(positions)


# Part 1
k1 = [[0, 0], [0, 0]]
print(getTailPositions(k1))

# Part 2
k2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
print(getTailPositions(k2))
