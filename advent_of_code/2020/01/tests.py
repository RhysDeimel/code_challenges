import solution as s

class TestUnit:
    def test_get_inputs(self):
        result = s.get_inputs("input.txt")
        assert result[0] == 1975
        assert result[-1] == 1322

    def test_find_nums_that_sum_to_can_handle_two_digits(self):
        given = [1721, 979, 366, 299, 675, 1456]
        expected = {1721, 299} # 2020
        result = s.find_nums_that_sum_to(given, 2, sum(expected)) 
        assert set(result) == expected

    def test_find_nums_that_sum_to_can_handle_three_digits(self):
        given = [1721, 979, 366, 299, 675, 1456]
        expected = {979, 366, 675} # 2020
        result = s.find_nums_that_sum_to(given, 3, sum(expected)) # 2020
        assert set(result) == expected


class TestFunctional:
    def test_program_one(self):
        given = [1721, 979, 366, 299, 675, 1456]
        expected = 514579

        assert s.program_one(given) == expected

    def test_program_two(self):
        given = [1721, 979, 366, 299, 675, 1456]
        expected = 241861950

        assert s.program_two(given) == expected