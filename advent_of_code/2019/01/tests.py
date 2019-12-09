import solution


class TestUnit:
    def test_get_inputs(self):
        result = solution.get_inputs("input.txt")
        assert result[0] == 60077
        assert result[-1] == 72622

    def test_simple_calc_module_fuel(self):
        assert solution.simple_calc_module_fuel(12) == 2
        assert solution.simple_calc_module_fuel(14) == 2
        assert solution.simple_calc_module_fuel(1969) == 654
        assert solution.simple_calc_module_fuel(100756) == 33583

    def test_calc_module_fuel(self):
        assert solution.calc_module_fuel(14) == 2
        assert solution.calc_module_fuel(1969) == 966
        assert solution.calc_module_fuel(100756) == 50346


class TestFunctional:
    def test_simple_solution_with_single_item(self):
        func = solution.simple_calc_module_fuel

        assert solution.solution([12], func) == 2
        assert solution.solution([14], func) == 2
        assert solution.solution([1969], func) == 654
        assert solution.solution([100756], func) == 33583

    def test_simple_solution_with_multiple_items(self):
        func = solution.simple_calc_module_fuel

        assert solution.solution([12, 14, 1969, 100756], func) == (2 + 2 + 654 + 33583)

    def test_solution_part_with_single_item(self):
        func = solution.calc_module_fuel

        assert solution.solution([14], func) == 2
        assert solution.solution([1969], func) == 966
        assert solution.solution([100756], func) == 50346

    def test_solution_part_two_with_multiple_items(self):
        func = solution.calc_module_fuel

        assert solution.solution([14, 1969, 100756], func) == (2 + 966 + 50346)
