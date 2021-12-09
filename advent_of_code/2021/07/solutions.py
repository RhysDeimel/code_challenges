import math
from collections import Counter


def parse(puzzle_input):
    return [int(num) for num in puzzle_input.rstrip().split(",")]


def part1(data):
    crabs = Counter(data)
    needed_fuel = {}

    for group in crabs.most_common():
        desired_pos = group[0]
        total_fuel = 0
        for pos, count in crabs.most_common():
            if pos == desired_pos:
                continue

            total_fuel += abs(desired_pos - pos) * count
        needed_fuel[desired_pos] = total_fuel

    return min(needed_fuel.values())


def part2(data):
    min_pos = min(data)
    max_pos = max(data)
    crabs = Counter(data)
    needed_fuel = {}

    for desired_pos in range(min_pos, max_pos + 1):
        total_fuel = 0
        for pos, count in crabs.most_common():
            if pos == desired_pos:
                continue
            n = abs(desired_pos - pos)
            total_fuel += (n * (n + 1) // 2) * count
        needed_fuel[desired_pos] = total_fuel

    return min(needed_fuel.values())


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
