def parse(puzzle_input):
    return [int(line) for line in puzzle_input.rstrip().split("\n")]


def part1(data):
    count = 0
    # Start at second value
    for i in range(1, len(data)):

        if data[i] > data[i - 1]:
            count += 1

    return count


def part2(data):
    count = 0
    # Start at the 4th value
    for i in range(3, len(data)):
        prev = sum(data[i - 3 : i])
        curr = sum(data[i - 2 : i + 1])

        if curr > prev:
            count += 1

    return count


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
