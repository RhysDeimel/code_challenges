from dataclasses import dataclass


def parse(puzzle_input):
    data = []
    for line in puzzle_input.rstrip().split("\n"):
        command, value = line.split(" ")
        data.append((command, int(value)))

    return data


@dataclass
class FirstComputer:
    program: list[tuple[str, int]]
    horizontal: int = 0
    vertical: int = 0

    def go(self):
        for item in self.program:
            match item:
                case ("forward", x):
                    self.horizontal += x
                case ("down", x):
                    self.vertical += x
                case ("up", x):
                    self.vertical -= x


@dataclass
class SecondComputer:
    program: list[tuple[str, int]]
    horizontal: int = 0
    vertical: int = 0
    aim: int = 0

    def go(self):
        for item in self.program:
            match item:
                case ("forward", x):
                    self.horizontal += x
                    self.vertical += self.aim * x
                case ("down", x):
                    self.aim += x
                case ("up", x):
                    self.aim -= x


def part1(data):
    submarine = FirstComputer(data)
    submarine.go()

    return submarine.horizontal * submarine.vertical


def part2(data):
    submarine = SecondComputer(data)
    submarine.go()

    return submarine.horizontal * submarine.vertical


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
