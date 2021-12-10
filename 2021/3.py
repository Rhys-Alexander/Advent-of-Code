from inpt import day3


# Part 1
def getPowerConsumption(bins):
    bin_length = len(bins[0])
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(bin_length):
        val = 0
        for bin in bins:
            if bin[i] == "1":
                val += 1
        gamma_rate += "1" if val >= (len(bins) / 2) else "0"
    for x in gamma_rate:
        epsilon_rate += "1" if x == "0" else "0"

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption


print(getPowerConsumption(day3()))


# Part 2
def getSingleBin(common, bins):
    for bit in range(len(bins[0])):
        if len(bins) == 1:
            break

        val = 0
        for bin in bins:
            if bin[bit] == "1":
                val += 1
        x, y = ("1", "0") if common else ("0", "1")
        common_bit = x if val >= (len(bins) / 2) else y

        new_bins = []
        for bin in bins:
            if bin[bit] == common_bit:
                new_bins.append(bin)
        bins = new_bins

    return bins[0]


def getLifeSupportRating(inpt):
    o2_gen_rating = getSingleBin(True, inpt)
    co2_scrub_rating = getSingleBin(False, inpt)
    life_support_rating = int(o2_gen_rating, 2) * int(co2_scrub_rating, 2)
    return life_support_rating


print(getLifeSupportRating(day3()))
