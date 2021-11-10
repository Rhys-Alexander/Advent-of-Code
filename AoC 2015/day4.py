import hashlib


# Part 1
def getHashNum5(inpt):
    i = 0
    while hashlib.md5(f"{inpt}{i}".encode("utf-8")).hexdigest()[:5] != "00000":
        i += 1
    return i


# Part 2
def getHashNum6(inpt):
    i = 0
    while hashlib.md5(f"{inpt}{i}".encode("utf-8")).hexdigest()[:6] != "000000":
        i += 1
    return i
