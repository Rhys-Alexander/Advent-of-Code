import random
import string


def getInput():
    inpt = "2,5,3,4,4,5,3,2,3,3,2,2,4,2,5,4,1,1,4,4,5,1,2,1,5,2,1,5,1,1,1,2,4,3,3,1,4,2,3,4,5,1,2,5,1,2,2,5,2,4,4,1,4,5,4,2,1,5,5,3,2,1,3,2,1,4,2,5,5,5,2,3,3,5,1,1,5,3,4,2,1,4,4,5,4,5,3,1,4,5,1,5,3,5,4,4,4,1,4,2,2,2,5,4,3,1,4,4,3,4,2,1,1,5,3,3,2,5,3,1,2,2,4,1,4,1,5,1,1,2,5,2,2,5,2,4,4,3,4,1,3,3,5,4,5,4,5,5,5,5,5,4,4,5,3,4,3,3,1,1,5,2,4,5,5,1,5,2,4,5,4,2,4,4,4,2,2,2,2,2,3,5,3,1,1,2,1,1,5,1,4,3,4,2,5,3,4,4,3,5,5,5,4,1,3,4,4,2,2,1,4,1,2,1,2,1,5,5,3,4,1,3,2,1,4,5,1,5,5,1,2,3,4,2,1,4,1,4,2,3,3,2,4,1,4,1,4,4,1,5,3,1,5,2,1,1,2,3,3,2,4,1,2,1,5,1,1,2,1,2,1,2,4,5,3,5,5,1,3,4,1,1,3,3,2,2,4,3,1,1,2,4,1,1,1,5,4,2,4,3"
    inpt = [int(x) for x in inpt.split(",")]
    # inpt = [3, 4, 3, 1, 2]
    return inpt


# Part 1
def getFishAfter80Days(fish_list):
    for d in range(80):
        for i, fish in enumerate(fish_list):
            if fish == 0:
                fish_list[i] = 6
                fish_list.append(9)
            else:
                fish_list[i] = fish - 1

    return len(fish_list)


# Part 2
# def getFishAfterDays(fish_list, days):
#     for i in fish_list:
#     key = random.choices(string.ascii_letters, k=10)
#     while key not in fish_dict.keys:
#         pass

#     for day in range(days):
#         for i, fish in enumerate(fish_list):
#             if fish == 0:
#                 fish_list[i] = 6
#                 fish_list.append(9)
#             else:
#                 fish_list[i] = fish - 1

#     return len(fish_list)


# print(getFishAfterDays(getInput(), 256))
