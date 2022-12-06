import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


@pytest.fixture
def example2():
    with open("example2.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


@pytest.fixture
def example3():
    with open("example3.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


@pytest.fixture
def example4():
    with open("example4.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


@pytest.fixture
def example5():
    with open("example5.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    assert example1 == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_part1_example1(example1):
    assert solutions.part1(example1) == 7


def test_part1_example2(example2):
    assert solutions.part1(example2) == 5


def test_part1_example3(example3):
    assert solutions.part1(example3) == 6


def test_part1_example4(example4):
    assert solutions.part1(example4) == 10


def test_part1_example5(example5):
    assert solutions.part1(example5) == 11


def test_part2_example1(example1):
    assert solutions.part2(example1) == 19


def test_part2_example2(example2):
    assert solutions.part2(example2) == 23


def test_part2_example3(example3):
    assert solutions.part2(example3) == 23


def test_part2_example4(example4):
    assert solutions.part2(example4) == 29


def test_part2_example5(example5):
    assert solutions.part2(example5) == 26
