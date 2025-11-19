import pytest
import numpy as np
from src.calculators.scientific_calculator import ScientificCalculator

calc = ScientificCalculator()

def test_power():
    assert calc.power(2, 3) == 8

def test_sqrt():
    assert calc.sqrt(16) == 4
    
def test_sqrt_negative():
    with pytest.raises(ValueError):
        calc.sqrt(-1)

def test_log_base_e():
    assert round(calc.log(np.e), 5) == 1.0

def test_log_base_10():
    assert round(calc.log(100, 10), 5) == 2.0

def test_log_base_e_precise():
    result = calc.log(np.e)
    assert abs(result - 1.0) < 1e-6
    
def test_log_zero():
    with pytest.raises(ValueError):
        calc.log(0)
    




