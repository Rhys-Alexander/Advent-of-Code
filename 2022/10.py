cycles = []
x = 1

for line in open("2022/10.txt"):
    if line.strip() == "noop":
        cycles.append(x)
    else:
        cycles.append(x)
        cycles.append(x)
        x += int(line.split()[1])

# Part 1
print(sum(cycles[i] * (i + 1) for i in range(len(cycles)) if (i - 19) % 40 == 0))

# Part 2
print(
    "\n".join(
        "".join(
            "#" if j in (x - 1, x, x + 1) else "."
            for j, x in enumerate(cycles[i * 40 : (i + 1) * 40])
        )
        for i in range(len(cycles) // 40)
    )
)
