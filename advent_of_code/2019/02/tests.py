import solution


class TestUnit:
    def test_get_inputs(self):
        result = solution.get_inputs("input.txt")
        assert result[0] == 1
        assert result[-1] == 0

    def test_add(self):
        given = [1, 0, 0, 0, 99]
        expected = [2, 0, 0, 0, 99]

        solution.add(given, 0)
        assert given == expected

    def test_multiply(self):
        given = [2, 3, 0, 3, 99]
        expected = [2, 3, 0, 6, 99]

        solution.multiply(given, 0)
        assert given == expected

    def test_multiply_again(self):
        given = [2,4,4,5,99,0]
        expected = [2,4,4,5,99,9801]

        solution.multiply(given, 0)
        assert given == expected

class TestFunctional:
    def test_program_one(self):
        given = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]

        solution.program_one(given)
        assert given == expected
