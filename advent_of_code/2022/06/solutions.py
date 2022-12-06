def parse(puzzle_input):
    return puzzle_input.strip()


def part1(data):
    for i in range(len(data) - 3):
        idx = i + 4
        if len(set(data[i:idx])) == 4:
            return idx


def part2(data):
    for i in range(len(data) - 13):
        idx = i + 14
        if len(set(data[i:idx])) == 14:
            return idx


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
