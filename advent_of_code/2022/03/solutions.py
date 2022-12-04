def parse(puzzle_input):
    return [line for line in puzzle_input.rstrip().split("\n")]


def priority(common: str):
    if common.isupper():
        return ord(common) - 38
    else:
        return ord(common) - 96


def part1(data):
    result = 0

    for line in data:
        half = len(line) // 2
        a = set(line[:half])
        b = set(line[half:])

        common = list(a & b)[0]
        result += priority(common)

    return result


def part2(data):
    def chunks(lst: list, n: int):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    result = 0

    for a, b, c in chunks(data, 3):
        common = list(set(a) & set(b) & set(c))[0]
        result += priority(common)

    return result


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
