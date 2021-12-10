from inpt import day10


def corrupted(line):
    chars = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for char in line:
        if char in chars.values():
            stack.append(char)
        elif stack.pop() != chars.get(char):
            return char
    return False


# Part 1
def getErrorScore(inpt):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return sum(scores.get(corrupted(line)) for line in inpt if corrupted(line))


# Part 2
def completeLines(inpt):
    uncorrupted = [line for line in inpt if not corrupted(line)]
    chars = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = list()
    for line in uncorrupted:
        stack = []
        for char in line:
            if char in chars.keys():
                stack.append(char)
            else:
                stack.pop()
        score = 0
        for char in reversed(stack):
            score = score * 5 + chars.get(char)
        scores.append(score)

    return sorted(scores)[len(scores) // 2]
