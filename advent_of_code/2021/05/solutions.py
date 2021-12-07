from collections import Counter


def parse(puzzle_input):
    lines = [line for line in puzzle_input.rstrip().split("\n")]

    data = []
    for line in lines:
        coords = line.replace(" -> ", ",")
        coords = coords.split(",")
        x1, y1, x2, y2 = [int(num) for num in coords]
        data.append([(x1, y1), (x2, y2)])
    return data


class HydrothermalVent:
    def __init__(self, coords):
        self.diagonal = False
        self.coords = coords
        self.segment = coords

    @property
    def segment(self):
        return self._segment

    def _is_diagonal(self, value):
        (x1, y1), (x2, y2) = value
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)
        return x_diff == y_diff

    def _diagonal_segment(self, value):
        (x1, y1), (x2, y2) = sorted(value)
        x_range = list(range(x1, x2 + 1))
        if y2 < y1:
            y_range = range(y1, y2 - 1, -1)
        else:
            y_range = range(y1, y2 + 1)

        return [f"{x},{y}" for x, y in zip(x_range, y_range)]

    @segment.setter
    def segment(self, value):
        (x1, y1), (x2, y2) = value
        if x1 == x2:
            y_min, y_max = sorted([y1, y2])
            self._segment = [f"{x1},{num}" for num in range(y_min, y_max + 1)]
        elif y1 == y2:
            x_min, x_max = sorted([x1, x2])
            self._segment = [f"{num},{y1}" for num in range(x_min, x_max + 1)]
        elif self._is_diagonal(value):
            self.diagonal = True
            self._segment = self._diagonal_segment(value)
        else:
            raise ValueError("Line not horizontal, vertical, or diagonal")


class OceanFloor:
    def __init__(self):
        self.grid = Counter()

    def __iadd__(self, other):
        self.grid.update(other.segment)
        return self

    def overlap(self):
        danger = [item for item in self.grid.items() if item[1] > 1]
        return len(danger)


def part1(data):
    ocean = OceanFloor()
    vents = []
    for coord in data:
        try:
            vent = HydrothermalVent(coord)
            if not vent.diagonal:
                vents.append(vent)
        except ValueError:
            pass

    for vent in vents:
        ocean += vent

    return ocean.overlap()


def part2(data):
    ocean = OceanFloor()
    vents = []
    for coord in data:
        try:
            vents.append(HydrothermalVent(coord))
        except ValueError:
            pass

    for vent in vents:
        ocean += vent

    return ocean.overlap()


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
