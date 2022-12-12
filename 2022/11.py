monkeys = []
x = 1


def getMonkeyBusiness(rounds, div=1):
    global x, monkeys
    monkeys = []
    for lines in open("2022/11.txt").read().split("\n\n"):
        items, op, test, t, f = lines.splitlines()[1:]
        test = int(test.split()[-1])
        x *= test
        items = [int(item) for item in items[18:].split(",")]
        op = eval(
            f"lambda old: monkeys[{t[-1]} if (({op[19:]}) // {div} % x ) % {test} == 0 else {f[-1]}][0].append(({op[19:]}) // {div} % x)"
        )
        monkeys.append([items, op, 0])

    for i in range(rounds):
        for m in monkeys:
            items, op, _ = m
            for item in items:
                op(item)
            m[-1] += len(items)
            m[0] = []

    a, b = sorted(monkey[-1] for monkey in monkeys)[-2:]
    return a * b


# Part 1
print(getMonkeyBusiness(20, 3))
