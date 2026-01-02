import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    assert list(example1) == [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]


def test_part1_example1(example1):
    assert solutions.part1(example1) == 3

def test_part2_example1(example1):
    ...