import solution


class TestUnit:
    def test_get_inputs(self):
        result = solution.get_inputs("input.txt")
        assert result[0] == 60077
        assert result[-1] == 72622

    def test_calc_module_fuel(self):
        assert solution.calc_module_fuel(12) == 2
        assert solution.calc_module_fuel(14) == 2
        assert solution.calc_module_fuel(1969) == 654
        assert solution.calc_module_fuel(100756) == 33583


class TestFunctional:
    def test_main_with_single_item(self):
        assert solution.main([12]) == 2
        assert solution.main([14]) == 2
        assert solution.main([1969]) == 654
        assert solution.main([100756]) == 33583

    def test_main_with_mutliple_items(self):
        assert solution.main([12, 14, 1969, 100756]) == (2 + 2 + 654 + 33583)
