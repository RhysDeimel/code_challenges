import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [
        [(0, 9), (5, 9)],
        [(8, 0), (0, 8)],
        [(9, 4), (3, 4)],
        [(2, 2), (2, 1)],
        [(7, 0), (7, 4)],
        [(6, 4), (2, 0)],
        [(0, 9), (2, 9)],
        [(3, 4), (1, 4)],
        [(0, 0), (8, 8)],
        [(5, 5), (8, 2)],
    ]


def test_part1_example1(example1):
    assert solutions.part1(example1) == 5


def test_part2_example1(example1):
    assert solutions.part2(example1) == 12
