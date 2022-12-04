import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    assert list(example1) == [
        [[2, 4], [6, 8]],
        [[2, 3], [4, 5]],
        [[5, 7], [7, 9]],
        [[2, 8], [3, 7]],
        [[6, 6], [4, 6]],
        [[2, 6], [4, 8]],
    ]


def test_part1_example1(example1):
    assert solutions.part1(example1) == 2


def test_part2_example1(example1):
    assert solutions.part2(example1) == 4
