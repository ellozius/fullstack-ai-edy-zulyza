import pytest
from src.calculators.basic_calculator import BasicCalculator

class TestBasicCalculator:
    def setup_method(self):
        self.calc = BasicCalculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5

    def test_subtract(self):
        assert self.calc.subtract(5, 2) == 3

    def test_multiply(self):
        assert self.calc.multiply(4, 3) == 12

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)
