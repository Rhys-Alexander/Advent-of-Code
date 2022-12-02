SCORES = {"X": 1, "Y": 2, "Z": 3}
OUTCOMES = {"A": ("Z", "X", "Y"), "B": ("X", "Y", "Z"), "C": ("Y", "Z", "X")}

# Part 1
def getTotalScore():
    return sum(
        (OUTCOMES[opp].index(player) * 3) + SCORES[player]
        for opp, player in (line.split() for line in open("2022/2.txt"))
    )


print(getTotalScore())
