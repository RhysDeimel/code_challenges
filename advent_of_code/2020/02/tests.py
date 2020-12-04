import solution as s


class TestUnit:
    def test_get_inputs(self):
        result = s.get_inputs("input.txt")
        assert result[0] == "5-11 t: glhbttzvzttkdx"
        assert result[-1] == "3-9 n: nnnlncrnnnnn"

    def test_process_inputs_creates_named_tuples(self):
        given = ["1-3 a: abcde", "1-3 b: cdefg"]
        result = s.process_inputs(given)

        assert result[0].min == 1
        assert result[0].max == 3
        assert result[0].letter == "a"
        assert result[0].password == "abcde"
        assert result[1].password == "cdefg"

    # def test_find_nums_that_sum_to_can_handle_three_digits(self):
    #     given = [1721, 979, 366, 299, 675, 1456]
    #     expected = {979, 366, 675}  # 2020
    #     result = s.find_nums_that_sum_to(given, 3, sum(expected))  # 2020
    #     assert set(result) == expected


class TestFunctional:
    def test_program_one(self):
        given = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

        assert s.program_one(given) == 2

    def test_program_two(self):
        given = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

        assert s.program_two(given) == 1
