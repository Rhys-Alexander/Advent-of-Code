from inpt import day14
from collections import defaultdict


# Part 1
def polymerization(inpt, steps):
    template, pairs = inpt
    for i in range(steps):
        inserts = list()
        for i, zp in enumerate(zip(template, template[1:])):
            chars = zp[0] + zp[1]
            if chars in pairs.keys():
                inserts.append((pairs[chars], i + 1))
        for insrt_i, insrt in enumerate(inserts):
            char, index = insrt
            template.insert(index + insrt_i, char)

    counts = [template.count(char) for char in set(template)]

    return max(counts) - min(counts)


print(polymerization(day14(), 10))


# Part 2
def quickPolymerization(inpt, steps):
    template, pairs = inpt
    template = ["".join(x) for x in zip(template, template[1:])]
    template = {x: template.count(x) for x in template}
    for _ in range(steps):
        new_template = defaultdict(int)
        for chars in template.keys():
            if chars in pairs.keys():
                iterations = template[chars]
                new_template[chars[0] + pairs[chars]] += iterations
                new_template[pairs[chars] + chars[1]] += iterations
        template = new_template
    char_counts = defaultdict(int)
    for pair, count in template.items():
        for char in pair:
            char_counts[char] += count
    vals = char_counts.values()

    return (max(vals) - min(vals) + 1) // 2


print(quickPolymerization(day14(), 40))
