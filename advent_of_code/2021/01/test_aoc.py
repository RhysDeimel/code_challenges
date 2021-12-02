import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1_example1(example1):
    assert solutions.part1(example1) == 7


def test_part2_example1(example1):
    assert solutions.part2(example1) == 5
