from inpt import day12


def sumPaths(part, neighbours, seen=set(), cave="start"):
    if cave in seen:
        if cave == "start":
            return 0
        elif cave.islower():
            if part == 1:
                return 0
            else:
                part = 1
    elif cave == "end":
        return 1
    return sum(sumPaths(part, neighbours, seen | {cave}, n) for n in neighbours[cave])


# Part 1
print(sumPaths(1, day12()))


# Part 2
print(sumPaths(2, day12()))
