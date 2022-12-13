import pprint


def parse(puzzle_input):
    return puzzle_input.rstrip().split("\n")


def part1(data):
    visible = []

    width = len(data[0])
    depth = len(data)

    x_blocked = []
    y_blocked = []

    # calc x (lock y)
    for iy, row in enumerate(data[1:-1], start=1):
        max = row[0]
        # forward
        for ix, tree in enumerate(row[1:-1], start=1):
            if iy in x_blocked:
                break

            if tree == 9:
                visible.append((ix, iy))
                x_blocked.append(iy)
            elif tree > max:
                visible.append((ix, iy))
                max = tree

        # reverse
        x_blocked.clear()
        max = row[-1]
        for ix, tree in enumerate(row[-2:0:-1], start=1):
            if iy in x_blocked:
                break

            x = width - ix - 1

            if tree == 9:
                visible.append((x, iy))
                x_blocked.append(iy)
            elif tree > max:
                visible.append((x, iy))
                max = tree

    # calc y (lock x)
    for ix in range(width - 2):
        x = ix + 1
        max = data[0][x]

        for iy, row in enumerate(data[1:-1], start=1):
            if x in y_blocked:
                break

            tree = row[x]

            if tree == 9:
                visible.append((x, iy))
                y_blocked.append(x)
            elif tree > max:
                visible.append((x, iy))
                max = tree

        # reverse
        y_blocked.clear()
        max = data[-1][x]
        for iy, row in enumerate(data[-2:0:-1], start=1):
            if x in y_blocked:
                break

            y = depth - iy - 1
            tree = row[x]

            if tree == 9:
                visible.append((x, y))
                y_blocked.append(x)
            elif tree > max:
                visible.append((x, y))
                max = tree

    pprint.pprint(set(visible))
    # minus 4 is to avoid double counting corners
    return (width * 2) + (depth * 2) - 4 + len(set(visible))


def part2(data):
    return None


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    print(f"Solution 1: {solution1}")
    print(f"Solution 2: {solution2}")


if __name__ == "__main__":
    with open("input.txt") as fd:
        puzzle_input = fd.read()

    solve(puzzle_input)
