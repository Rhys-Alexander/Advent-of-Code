from inpt import day14
from collections import defaultdict

# TODO try with Counter


def polymerization(inpt, steps):
    template, rules = inpt
    for _ in range(steps):
        new_template = defaultdict(int)
        for chars in template.keys():
            if chars in rules.keys():
                iterations = template[chars]
                new_template[chars[0] + rules[chars]] += iterations
                new_template[rules[chars] + chars[1]] += iterations
        template = new_template
    char_counts = defaultdict(int)
    for pair, count in template.items():
        for char in pair:
            char_counts[char] += count
    vals = char_counts.values()

    return (max(vals) - min(vals) + 1) // 2


# Part 1
print(polymerization(day14(), 10))


# Part 2
print(polymerization(day14(), 40))
