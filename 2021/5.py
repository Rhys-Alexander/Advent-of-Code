class Position(object):
    def __init__(self, cood):
        x, y = cood
        self.x = x
        self.y = y

    def __add__(self, tup):
        tup_x, tup_y = tup
        return Position((self.x + tup_x, self.y + tup_y))

    def __iadd__(self, tup):
        # Works for +=
        tup_x, tup_y = tup
        self.x += tup_x
        self.y += tup_y
        return self

    __radd__ = __add__

    def __str__(self):
        "Define the textual representation of a Position"
        return "Position(x=%d, y=%d)" % (self.x, self.y)

    __repr__ = __str__

    def getCood(self):
        return (self.x, self.y)


# Part 1
def getOverlapsStraight(instrs):
    visited = set()
    overlaps = set()
    instrs = [
        coods
        for coods in instrs
        if (coods[0][0] == coods[1][0] or coods[0][1] == coods[1][1])
    ]

    for coods in instrs:
        x_diff, y_diff = (coods[1][0] - coods[0][0]), (coods[1][1] - coods[0][1])
        getStep = lambda diff: (abs(diff) % (diff - 1)) if diff != 2 else 1
        step = (getStep(x_diff), getStep(y_diff))

        sortLocation = (
            lambda location: overlaps.add(location.getCood())
            if (location.getCood() in visited) and (location.getCood() not in overlaps)
            else visited.add(location.getCood())
        )

        current_location = Position(coods[0])
        sortLocation(current_location)

        while current_location.getCood() != coods[1]:
            current_location += step
            sortLocation(current_location)

    return len(overlaps)


# Part 2
def getOverlaps(instrs):
    visited = set()
    overlaps = set()
    for coods in instrs:
        x_diff, y_diff = (coods[1][0] - coods[0][0]), (coods[1][1] - coods[0][1])
        getStep = lambda diff: (abs(diff) % (diff - 1)) if diff != 2 else 1
        step = (getStep(x_diff), getStep(y_diff))

        sortLocation = (
            lambda location: overlaps.add(location.getCood())
            if (location.getCood() in visited) and (location.getCood() not in overlaps)
            else visited.add(location.getCood())
        )

        current_location = Position(coods[0])
        sortLocation(current_location)

        while current_location.getCood() != coods[1]:
            current_location += step
            sortLocation(current_location)

    return len(overlaps)
