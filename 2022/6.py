def getMarker(l):
    s = open("2022/6.txt").read()
    for i in range(len(s) - l + 1):
        if len(set(s[i : i + l])) == l:
            return i + l


# Part 1
print(getMarker(4))
# Part 2
print(getMarker(14))

# All of day 6 in 98 chars
#
# for l in (4,14):
#  for i in range(9999):
#   if len(set(open("6").read()[i:i+l]))==l:print(i+l);break
