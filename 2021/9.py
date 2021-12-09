from math import prod


# Part 1
def sumLowPoints(inpt):
    for line in inpt:
        line.append(9)
    inpt.insert(len(inpt), [9 for x in inpt[0]])
    return sum(
        sum(
            num + 1
            for num_i, num in enumerate(line[:-1])
            if num
            < min(
                line[num_i + 1],
                line[num_i - 1],
                inpt[line_i + 1][num_i],
                inpt[line_i - 1][num_i],
            )
        )
        for line_i, line in enumerate(inpt[:-1])
    )


# Part 2
def sum3LargestBasins(inpt):
    for line in inpt:
        line.append(9)
    inpt.insert(len(inpt), [9 for x in inpt[0]])

    low_points = [
        item
        for sublist in [
            [
                (num_i, line_i)
                for num_i, num in enumerate(line[:-1])
                if num
                < min(
                    line[num_i + 1],
                    line[num_i - 1],
                    inpt[line_i + 1][num_i],
                    inpt[line_i - 1][num_i],
                )
            ]
            for line_i, line in enumerate(inpt[:-1])
        ]
        for item in sublist
    ]

    basins = list()
    for low_point in low_points:
        basin_points = [low_point]
        for point in basin_points:
            num_i, line_i = point
            if inpt[line_i][num_i + 1] < 9 and (
                (num_i + 1, line_i) not in basin_points
            ):
                basin_points.append((num_i + 1, line_i))
            if inpt[line_i][num_i - 1] < 9 and (
                (num_i - 1, line_i) not in basin_points
            ):
                basin_points.append((num_i - 1, line_i))
            if inpt[line_i + 1][num_i] < 9 and (
                (num_i, line_i + 1) not in basin_points
            ):
                basin_points.append((num_i, line_i + 1))
            if inpt[line_i - 1][num_i] < 9 and (
                (num_i, line_i - 1) not in basin_points
            ):
                basin_points.append((num_i, line_i - 1))
        basins.append(len(basin_points))

    return prod(sorted(basins)[-3:])
