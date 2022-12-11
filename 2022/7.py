dirs = dict()
currentDir = ""

for line in open("2022/7.txt").readlines():
    split = line.split()
    if split[1] == "cd" and split[2] != "..":
        currentDir += (
            "/" + split[2] if currentDir != "/" and split[2] != "/" else split[2]
        )
        dirs[currentDir] = []
    elif split[1] == "cd":
        currentDir = "/".join(currentDir.split("/")[:-1])
    elif split[1] != "ls":
        dirs[currentDir].append(
            int(split[0])
            if split[0].isdigit()
            else currentDir
            + ("/" + split[1] if currentDir != "/" and split[1] != "/" else split[1])
        )


def getDirSize(dir):
    size = 0
    for item in dirs[dir]:
        if isinstance(item, int):
            size += item
        else:
            size += getDirSize(item)
    return size


# Part 1
print(sum(getDirSize(key) for key in dirs.keys() if getDirSize(key) <= 100000))
