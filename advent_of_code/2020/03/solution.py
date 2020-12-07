def get_inputs(file):
    with open(file, "r") as fd:
        return fd.read().splitlines()


def find_trees(vector, grid):
    max_width = len(grid[0])

    num_trees = 0

    x_pos = 0
    y_pos = 0

    while True:
        x_pos += vector[0]
        y_pos += vector[1]

        try:
            if grid[y_pos][x_pos % max_width] == "#":
                num_trees += 1

        except IndexError:
            return num_trees


def program_one(grid):
    return find_trees((3, 1), grid)


def program_two(grid):
    def tree_product(vectors, grid):
        prod = 1
        for vec in vectors:
            prod *= find_trees(vec, grid)
        return prod

    vectors = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return tree_product(vectors, grid)


if __name__ == "__main__":
    inputs = get_inputs("input.txt")
    print(f"Part one solution: {program_one(inputs)}")
    print(f"Part two solution: {program_two(inputs)}")
