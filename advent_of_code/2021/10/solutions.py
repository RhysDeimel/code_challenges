def parse(puzzle_input):
    lines = [line for line in puzzle_input.rstrip().split("\n")]
    return lines


def part1(data):
    illegal = []

    for line in data:
        closing = []
        for char in line:

            match char:
                case "(":
                    closing.append(")")
                case "[":
                    closing.append("]")
                case "{":
                    closing.append("}")
                case "<":
                    pass
                    closing.append(">")
                case ")" | "]" | "}" | ">":
                    if not closing.pop() == char:
                        illegal.append(char)
                        continue

    score = 0
    for char in illegal:
        match char:
            case ")":
                score += 3
            case "]":
                score += 57
            case "}":
                score += 1197
            case ">":
                score += 25137

    return score


def part2(data):
    incomplete = []

    for line in data:
        closing = []
        corrupted = False
        for char in line:

            match char:
                case "(":
                    closing.append(")")
                case "[":
                    closing.append("]")
                case "{":
                    closing.append("}")
                case "<":
                    pass
                    closing.append(">")
                case ")" | "]" | "}" | ">":
                    if not closing.pop() == char:
                        corrupted = True
                        continue

        if not corrupted:
            incomplete.append(closing)

    scores = []
    for sequence in incomplete:
        score = 0
        for char in sequence[::-1]:
            score *= 5
            match char:
                case ")":
                    score += 1
                case "]":
                    score += 2
                case "}":
                    score += 3
                case ">":
                    score += 4

        scores.append(score)

    scores = sorted(scores)
    middle = len(scores) // 2
    return scores[middle]


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
