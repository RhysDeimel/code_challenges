import itertools
import math


def get_inputs(file):
    with open(file, "r") as fd:
        lines = fd.readlines()
        return [int(num) for num in lines]


def find_nums_that_sum_to(items, n_entries, sum_to):
    combinations = [
        subsequence for subsequence in itertools.combinations(items, n_entries)
    ]
    sums = [sum(element) for element in combinations]
    return combinations[sums.index(sum_to)]


def program_one(inputs):
    nums = find_nums_that_sum_to(inputs, 2, 2020)
    return math.prod(nums)


def program_two(inputs):
    nums = find_nums_that_sum_to(inputs, 3, 2020)
    return math.prod(nums)
    pass


if __name__ == "__main__":
    inputs = get_inputs("input.txt")
    print(f"Part one solution: {program_one(inputs)}")
    print(f"Part two solution: {program_two(inputs)}")
