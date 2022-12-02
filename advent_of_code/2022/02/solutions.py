WIN = 6
DRAW = 3


def parse(puzzle_input):
    return [tuple(line.split(" ")) for line in puzzle_input.rstrip().split("\n")]


def shape_points(shape):
    match shape:
        case ("X" | "A"):
            return 1
        case ("Y" | "B"):
            return 2
        case ("Z" | "C"):
            return 3


def part1(data):
    # offset by one relationship
    # A or X = Rock
    # B or Y = Paper
    # C or Z = Scissors
    result = 0

    for round in data:
        result += shape_points(round[1])
        match round:
            case (("C", "X") | ("A", "Y") | ("B", "Z")):
                # player win
                result += WIN

            case (("A", "X") | ("B", "Y") | ("C", "Z")):
                # player draw
                result += DRAW

    return result


def part2(data):
    shapes = ["A", "B", "C"]

    def choose_shape(outcome):
        pos = (shapes.index(oppenent) + outcome) % 3
        return shapes[pos]

    result = 0
    for oppenent, outcome in data:
        offset = -1
        match (oppenent, outcome):
            case (_, "Y"):
                # player draw
                offset = 0
                result += DRAW
            case (_, "Z"):
                # player win
                offset = 1
                result += WIN

        result += shape_points(choose_shape(offset))

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
