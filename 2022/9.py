instrs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
h, t = [0, 0], [0, 0]
positions = set()

for line in open("2022/t.txt"):
    instr, val = line.strip().split()
    for i in range(int(val)):
        h[0] += instrs[instr][0]
        h[1] += instrs[instr][1]
        if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
            t = [h[0] - instrs[instr][0], h[1] - instrs[instr][1]]
        positions.add(tuple(t))

print(len(positions))
