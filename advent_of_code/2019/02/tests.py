import solution


class TestUnit:
    def test_get_inputs(self):
        result = solution.get_inputs("input.txt")
        assert result[0] == 1
        assert result[-1] == 0

    def test_add(self):
        test_ints = [0 for _ in range(31)]
        test_ints[0:3] = 1, 10, 20, 30

        assert solution.add(test_ints, 0)

class TestFunctional():
    pass