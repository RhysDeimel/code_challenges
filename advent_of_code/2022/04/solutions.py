def parse(puzzle_input):
    lines = [line for line in puzzle_input.rstrip().split("\n")]
    data = []
    for line in lines:
        line = line.replace("-", ",")
        sections = list(map(int, line.split(",")))
        data.append([sections[:2], sections[2:]])

    return data


def part1(data):
    result = 0

    for elf_a, elf_b in data:
        start, end = elf_a
        elf_a_sections = set(range(start, end + 1))

        start, end = elf_b
        elf_b_sections = set(range(start, end + 1))

        if (elf_a_sections <= elf_b_sections) or (elf_b_sections <= elf_a_sections):
            result += 1

    return result


def part2(data):
    result = 0

    for elf_a, elf_b in data:
        start, end = elf_a
        elf_a_sections = set(range(start, end + 1))

        start, end = elf_b
        elf_b_sections = set(range(start, end + 1))

        if elf_a_sections & elf_b_sections:
            result += 1

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
