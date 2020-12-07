def get_inputs(file):
    with open(file, "r") as fd:
        return fd.read().splitlines()


def program_one(grid):
    # right 3, down one
    width = len(grid[0])
    num_trees = 0
    x_pos = 0
    for row in grid:
        if row[x_pos % width] == "#":
            num_trees += 1
        x_pos += 3

    return num_trees


def program_two(inputs):
    pass


if __name__ == "__main__":
    inputs = get_inputs("input.txt")
    print(f"Part one solution: {program_one(inputs)}")
    # print(f"Part two solution: {program_two(inputs)}")
