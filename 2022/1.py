# Part 1
print(
    max(
        sum(int(x) for x in elf.split("\n"))
        for elf in open("2022/1.txt").read().split("\n\n")
    )
)

# Part 2
print(
    sum(
        sorted(
            sum(int(x) for x in elf.split("\n"))
            for elf in open("2022/1.txt").read().split("\n\n")
        )[-3:]
    )
)
