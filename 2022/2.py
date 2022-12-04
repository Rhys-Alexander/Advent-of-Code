SCORES = {"X": 1, "Y": 2, "Z": 3}
OUTCOMES = {"A": ("Z", "X", "Y"), "B": ("X", "Y", "Z"), "C": ("Y", "Z", "X")}

# Part 1
print(
    sum(
        (OUTCOMES[opp].index(player) * 3) + SCORES[player]
        for opp, player in (line.split() for line in open("2022/2.txt"))
    )
)


# Part 2
print(
    sum(
        SCORES[OUTCOMES[opp][SCORES[outcome] - 1]] + (SCORES[outcome] - 1) * 3
        for opp, outcome in (line.split() for line in open("2022/2.txt"))
    )
)
