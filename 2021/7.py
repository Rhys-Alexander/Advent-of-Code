from inpt import day7
from numpy import *

# Part 1
def getFuel(inpt):
    # Sums list of differences between the median of a list and its elements.
    return int(sum(abs(inpt - median(inpt))))


print(getFuel(day7()))


# Part 2
def getFuelIncrease(inpt):
    # fuel returns sum of all consecutive numbers up until and including 'd'
    fuel = lambda d: d * (d + 1) / 2
    sum_fuel = lambda x: sum(fuel(abs(inpt - x(mean(inpt)))))
    # gets minimum value of wether the mean was floored or ceiled
    return int(min(sum_fuel(floor), sum_fuel(ceil)))


print(getFuelIncrease(day7()))
