inpt = "L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"
instructions = inpt.split(", ")


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        "In-place add += updates the current instance."
        self.x += other.x
        self.y += other.y
        return self

    __radd__ = __add__

    def __str__(self):
        "Define the textual representation of a Position"
        return "Position(x=%d, y=%d)" % (self.x, self.y)

    __repr__ = __str__


def changeDirection(char, direction):
    if char == "R":
        direction += 1
    else:
        direction -= 1
    direction %= 4

    return direction


def getDistance(tuple):
    x, y = tuple[0], tuple[1]
    distance = abs(x) + abs(y)
    return distance


# Part 1
def getBlocksAway(instrs):
    current_location = Position(0, 0)
    direction = 0
    steps = [Position(0, 1), Position(1, 0), Position(0, -1), Position(-1, 0)]

    for instr in instrs:
        direction = changeDirection(instr[0], direction)
        step = steps[direction]

        distance = int(instr[1:])

        for i in range(distance):
            current_location += step

    current_location_tuple = (current_location.x, current_location.y)
    return current_location_tuple


# Part 2
def getIfVistedTwice(instrs):
    visited = set({(0, 0)})
    direction = 0
    current_location = Position(0, 0)
    steps = [Position(0, 1), Position(1, 0), Position(0, -1), Position(-1, 0)]

    for instr in instrs:
        direction = changeDirection(instr[0], direction)
        step = steps[direction]
        distance = int(instr[1:])

        for i in range(distance):
            current_location += step
            stop = (current_location.x, current_location.y)
            if stop in visited:
                return stop
            visited.add(stop)
