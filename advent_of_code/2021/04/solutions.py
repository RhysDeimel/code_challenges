def parse(puzzle_input):
    lines = [line for line in puzzle_input.rstrip().split("\n")]
    numbers = [int(num) for num in lines[0].split(",")]
    boards = []
    temp = []
    for line in lines[2:]:
        if not line:
            boards.append(temp)
            temp = []
            continue
        row = [int(num) for num in line.split()]
        temp.append(row)

    boards.append(temp)

    return [numbers] + boards


class BingoBoard:
    def __init__(self, data):
        self.grid = data
        self.won = False

    def _horizontal(self):
        for row in self.grid:
            if set(row).issubset(self.numbers):
                return True

    def _vertical(self):
        for i in range(len(self.grid[0])):
            column = []

            for row in self.grid:
                column.append(row[i])

            if set(column).issubset(self.numbers):
                return True

    def sum_unmarked(self):
        unmarked = 0
        for row in self.grid:
            unmarked += sum(set(row) - self.numbers)

        return unmarked

    def has_won(self, numbers):
        self.numbers = set(numbers)
        if self._horizontal() or self._vertical():
            self.won = True
            return self.sum_unmarked()


def part1(data):
    numbers = data[0][:]
    boards = [BingoBoard(board) for board in data[1:]]

    drawn_numbers = []
    for i in range(5):
        drawn_numbers.append(numbers.pop(0))

    while True:
        for board in boards:
            if board.has_won(drawn_numbers):
                return board.sum_unmarked() * drawn_numbers[-1]

        try:
            drawn_numbers.append(numbers.pop(0))
        except IndexError:
            break


def part2(data):
    numbers = data[0][:]
    boards = [BingoBoard(board) for board in data[1:]]

    winning_boards = []
    drawn_numbers = []
    for i in range(5):
        drawn_numbers.append(numbers.pop(0))

    while True:
        for board in boards:
            if board.won:
                continue

            if board.has_won(drawn_numbers):
                winning_boards.append(board)
                if len(winning_boards) == len(boards):
                    return board.sum_unmarked() * drawn_numbers[-1]

        try:
            drawn_numbers.append(numbers.pop(0))
        except IndexError:
            break


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
