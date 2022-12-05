import copy


def parse(puzzle_input):
    raw_crates, raw_moves = puzzle_input.rstrip().split("\n\n")
    crates = []
    moves = []

    # get the number of the last column
    num_columns = int(raw_crates[-1])
    raw_crates = raw_crates.split("\n")
    line_length = len(raw_crates[-1]) + 1
    # remove numbered column
    raw_crates = raw_crates[:-1]
    for row in raw_crates:
        if (cur_len := len(row)) < line_length:
            # equalise lines
            row += " " * (line_length - cur_len)
        # ignore the brackets
        crates.append([letter for letter in row[1::4]])

    raw_moves = [line for line in raw_moves.split("\n")]
    for line in raw_moves:
        items = line.split(" ")
        nums_only = list(map(int, [items[1], items[3], items[5]]))
        moves.append(nums_only)

    return crates, moves


class Ship:
    def __init__(self, crates: list):
        self.crates = copy.deepcopy(crates)

    def pick(self, column: int):
        for row in self.crates:
            if (held := row[column - 1]) != " ":
                self.held = held
                row[column - 1] = " "
                return

    def place(self, column: int):
        for row in self.crates[::-1]:
            if row[column - 1] == " ":
                row[column - 1] = self.held
                self.held = None
                return

        new_row = [" " for pos in self.crates[0]]
        self.crates.insert(0, new_row)
        self.place(column)

    def top_crates(self):
        data = ""
        for i, column in enumerate(self.crates[0]):
            for row in self.crates:
                if (letter := row[i]) != " ":
                    data += letter
                    break

        return data


class Ship2:
    def __init__(self, crates: list):
        self.crates = copy.deepcopy(crates)
        self.held = []

    def pick(self, num: int, column: int):
        for row in self.crates:
            if num > 0 and row[column - 1] != " ":
                self.held.append(row[column - 1])
                row[column - 1] = " "
                num -= 1

    def place(self, column: int):
        for row in self.crates[::-1]:
            if row[column - 1] == " ":
                try:
                    row[column - 1] = self.held.pop()
                except IndexError:
                    return

        if self.held:
            new_row = [" " for pos in self.crates[0]]
            self.crates.insert(0, new_row)
            self.place(column)

    def top_crates(self):
        data = ""
        for i, column in enumerate(self.crates[0]):
            for row in self.crates:
                if (letter := row[i]) != " ":
                    data += letter
                    break

        return data


def part1(data):
    crates, moves = data

    ship = Ship(crates)

    for num, from_pos, to_pos in moves:
        for i in range(num):  # move this many crates
            ship.pick(from_pos)
            ship.place(to_pos)

    return ship.top_crates()


def part2(data):
    crates, moves = data

    ship = Ship2(crates)

    for num, from_pos, to_pos in moves:
        ship.pick(num, from_pos)
        ship.place(to_pos)

    return ship.top_crates()


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
