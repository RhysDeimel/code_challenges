def parse(puzzle_input):
    return puzzle_input.strip().split("\n")


def part1(data):
    password = 0
    dial = 50
    dial_range = 100

    for line in data:
        match line[0], int(line[1:]):
            case ["L", num]:
                dial = (dial - num) % dial_range
            case ["R", num]:
                dial = (dial + num) % dial_range

        if dial == 0:
            password += 1

    return password

def part2(data):
    ...


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
