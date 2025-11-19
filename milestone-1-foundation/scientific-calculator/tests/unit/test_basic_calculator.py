import pytest
from src.calculators.basic_calculator import BasicCalculator

calc  = BasicCalculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    
def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(-1, -1) == 0

def test_multiply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(0, 100) == 0

def test_divide():
    assert calc.divide(6, 3) == 2
    assert calc.divide(-4, 2) == -2
    assert calc.divide(5, 2) == 2.5
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)
        
        
        
        