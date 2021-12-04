from collections import Counter


def parse(puzzle_input):
    return [binary_str for binary_str in puzzle_input.rstrip().split("\n")]


def part1(data):
    gamma = ""
    epsilon = ""

    for pos in range(0, len(data[0])):
        nums = [binary_str[pos] for binary_str in data]
        count = Counter(nums)

        if count["0"] > count["1"]:
            gamma += "0"
            epsilon += "1"

        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    def _get_rating(bit):
        if bit == "1":
            measure = 0
        else:
            measure = 1

        binary = data[:]
        for pos in range(0, len(data[0])):
            if len(binary) == 1:
                break
            temp_binary = []
            nums = [binary_str[pos] for binary_str in binary]
            count = Counter(nums)

            counts = count.most_common()
            if counts[0][1] == counts[1][1]:
                common = bit
            else:
                common = counts[measure][0]

            for num in binary:
                if num[pos] == common:
                    temp_binary.append(num)

            binary = temp_binary[:]

        return binary[0]

    o2_rating = _get_rating("1")
    co2_rating = _get_rating("0")

    return int(o2_rating, 2) * int(co2_rating, 2)


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
