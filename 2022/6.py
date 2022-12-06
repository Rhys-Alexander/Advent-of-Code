def getMarker(l):
    s = open("2022/6.txt").read()
    for i in range(len(s) - l + 1):
        if len(set(s[i : i + l])) == l:
            return i + l


# Part 1
print(getMarker(4))
