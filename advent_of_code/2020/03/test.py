import solution as s

test_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


class TestUnit:
    def test_get_inputs(self):
        result = s.get_inputs("input.txt")
        assert result[0] == ".....#.........#...#..##....#.."
        assert result[-1] == "..#..#........#...#.......#...."

    def test_find_trees_1_1_gives_2(self):
        assert s.find_trees((1, 1), test_input) == 2

    def test_find_trees_3_1_gives_7(self):
        assert s.find_trees((3, 1), test_input) == 7

    def test_find_trees_5_1_gives_3(self):
        assert s.find_trees((5, 1), test_input) == 3

    def test_find_trees_7_1_gives_4(self):
        assert s.find_trees((7, 1), test_input) == 4

    def test_find_trees_1_2_gives_2(self):
        assert s.find_trees((1, 2), test_input) == 2


class TestFunctional:
    def test_program_one(self):

        assert s.program_one(test_input) == 7

    def test_program_two(self):

        assert s.program_two(test_input) == 336
