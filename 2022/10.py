cycles = []
x = 1

for line in open("2022/t.txt"):
    if line.strip() == "noop":
        cycles.append(x)
    else:
        cycles.append(x)
        cycles.append(x)
        x += int(line.split()[1])

print(sum(cycles[i - 1] * (i) for i in range(len(cycles)) if (i - 20) % 40 == 0))
