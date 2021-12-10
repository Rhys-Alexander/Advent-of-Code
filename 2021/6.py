from inpt import day6
import random
import string


def getPopulation(init_state, days):
    state = [init_state.count(i) for i in range(9)]
    for _ in range(days):
        state = state[1:] + state[:1]
        state[6] += state[8]
    return sum(state)


# Part 1
print(getPopulation(day6(), 80))


# Part 2
print(getPopulation(day6(), 256))
