from inpt import day8


# Part 1
def get1478(inpt):
    return sum([len([1 for y in x[1] if len(y) in [2, 3, 4, 7]]) for x in inpt])


print(get1478(day8()))


# Part 2
def sumVals(inpt):
    sums = {
        42: "0",
        17: "1",
        34: "2",
        39: "3",
        30: "4",
        37: "5",
        41: "6",
        25: "7",
        49: "8",
        45: "9",
    }
    return sum(
        int(
            "".join(
                sums.get(sum(sum(segment.count(x) for segment in line[0]) for x in seg))
                for seg in line[1]
            )
        )
        for line in inpt
    )


print(sumVals(day8()))
