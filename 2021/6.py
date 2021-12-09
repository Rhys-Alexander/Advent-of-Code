import random
import string


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
def getPopulation(init_state, days):
    state = [init_state.count(i) for i in range(9)]
    for _ in range(days):
        state = state[1:] + state[:1]
        state[6] += state[8]
    return sum(state)
