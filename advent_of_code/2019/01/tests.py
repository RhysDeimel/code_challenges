import solution


class TestUnit:
    def test_get_inputs(self):
        result = solution.get_inputs("input.txt")
        assert result[0] == 60077
        assert result[-1] == 72622

    def test_calc_module_fuel(self):
        assert solution.simple_calc_module_fuel(12) == 2
        assert solution.simple_calc_module_fuel(14) == 2
        assert solution.simple_calc_module_fuel(1969) == 654
        assert solution.simple_calc_module_fuel(100756) == 33583


class TestFunctional:
    def test_soultion_part_one_with_single_item(self):
        assert solution.soultion_part_one([12]) == 2
        assert solution.soultion_part_one([14]) == 2
        assert solution.soultion_part_one([1969]) == 654
        assert solution.soultion_part_one([100756]) == 33583

    def test_soultion_part_one_with_mutliple_items(self):
        assert solution.soultion_part_one([12, 14, 1969, 100756]) == (2 + 2 + 654 + 33583)
