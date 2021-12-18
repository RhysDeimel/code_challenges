def parse(puzzle_input):
    lines = [[int(num) for num in line] for line in puzzle_input.rstrip().split("\n")]
    return lines


class Point:
    def __init__(self, grid, origin):
        self.grid = grid
        self._max_x = len(grid[0])
        self._max_y = len(grid)
        self.origin = origin
        self.height = grid[origin[1]][origin[0]]
        self.risk = self.height + 1
        self.basin_coords = []

    @property
    def surrounds(self):
        x, y = self.origin
        surrounds = []

        for coord in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            x, y = coord
            if not -1 < x < self._max_x:
                continue
            if not -1 < y < self._max_y:
                continue

            surrounds.append(coord)

        return surrounds

    @property
    def low(self):
        data = [self.grid[y][x] for x, y in self.surrounds]
        return min(data) > self.height

    @property
    def basin(self):
        if self.low:
            self._calc_basin()
            return len(self.basin_coords)
        else:
            return None

    def _calc_basin(self, origin=None):
        if not origin:
            origin = self.origin

        x, y = origin
        if not (-1 < x < self._max_x and -1 < y < self._max_y):
            return None

        height = self.grid[y][x]
        if height == 9:
            return

        if origin in self.basin_coords:
            return

        self.basin_coords.append(origin)

        for item in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            self._calc_basin(item)


def part1(data):
    points = [
        Point(data, (x, y)) for y in range(len(data)) for x in range(len(data[0]))
    ]

    lows = [point.risk for point in points if point.low]

    return sum(lows)


def part2(data):
    points = [
        Point(data, (x, y)) for y in range(len(data)) for x in range(len(data[0]))
    ]

    basins = [point.basin for point in points if point.low]
    basins = sorted(basins, reverse=True)
    result = 1

    for basin in basins[:3]:
        result *= basin

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
