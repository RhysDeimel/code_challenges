import solution

class TestUnit:
    def test_get_inputs(self):
        result = solution.get_inputs("input.txt")
        assert result[0] == 1975
        assert result[-1] == 1322

# class TestFunctional:
#     def test_program_one(self):
#         given = [1, 1, 1, 4, 99, 5, 6, 0, 99]
#         expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]

#         solution.program_one(given)
#         assert given == expected