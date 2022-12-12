from collections import deque


def parse(puzzle_input):
    return puzzle_input.rstrip().split("\n")


class File:
    def __init__(self, name: str, parent: object, size: int = None):
        self.name = name
        self.parent = parent
        self.children = dict()
        self._size = size

    @property
    def size(self):
        return self._size

    @size.getter
    def size(self):
        if not self._size:
            total = 0
            for child in self.children.values():
                total += child.size

            return total
        else:
            return self._size

    def __repr__(self):
        return self.name

    def __radd__(self, other):
        return self.size + other


def part1(data):
    root = File(name="/", parent=None)

    nodes = deque()
    head = None

    for line in data:
        match line.split(" "):
            case ("$", "ls"):
                pass

            case ("$", "cd", ".."):
                head = nodes.pop()

            case ("$", "cd", "/"):
                nodes.clear()
                head = root

            case ("$", "cd", folder):
                nodes.append(head)
                head = head.children[folder]

            case ("dir", folder):
                if not folder in head.children.keys():
                    head.children[folder] = File(name=folder, parent=head)

            case (size, file_name):
                if not file_name in head.children.keys():
                    head.children[file_name] = File(
                        name=file_name, parent=head, size=int(size)
                    )

    def all_directories(folder):
        directories = []
        for child in folder.children.values():
            if not child._size:
                directories.append(child)
                directories += all_directories(child)

        return directories

    directories = []
    for dir in all_directories(root):
        if (dir_size := dir.size) <= 100000:
            directories.append(dir)

    return sum(directories)


def part2(data):
    return None


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
