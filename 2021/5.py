def getInput():
    pass


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
