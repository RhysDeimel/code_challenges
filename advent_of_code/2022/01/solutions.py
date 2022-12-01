def parse(puzzle_input):
    return [[int(item) for item in line.split("\n")] for line in puzzle_input.rstrip().split("\n\n")]


def part1(data):
    return max([sum(chunk) for chunk in data])


def part2(data):
    top_three = sorted([sum(chunk) for chunk in data], reverse=True)[:3]
    return sum(top_three)


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
