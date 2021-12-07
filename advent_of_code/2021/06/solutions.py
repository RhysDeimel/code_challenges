from collections import Counter, defaultdict


def parse(puzzle_input):
    return [int(num) for num in puzzle_input.rstrip().split(",")]


class Lanternfish:
    def __init__(self, timer=8):
        self.timer = timer

    def __isub__(self, other):
        if self.timer == 0:
            self.timer = 6
        else:
            self.timer -= 1

        return self


def part1(data):
    # Fun solution
    fishies = [Lanternfish(num) for num in data]

    for day in range(80):
        hatchlings = []
        for fish in fishies:
            if fish.timer == 0:
                hatchlings.append(Lanternfish())
            fish -= 1

        fishies += hatchlings

    return len(fishies)


def part2(data):
    # Scalable solution
    fishies = Counter(data)

    for day in range(256):
        temp = {x: 0 for x in range(9)}
        for item in fishies.items():
            match item:
                case (0, x):
                    temp[8] += x
                    temp[6] += x
                    continue
                case _:
                    timer, count = item
                    timer -= 1
                    temp[timer] += count

        fishies = temp.copy()

    return sum(fishies.values())


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
