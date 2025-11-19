import numpy as np
from src.calculators.base_calculator import BaseCalculator

class ScientificCalculator(BaseCalculator):
    '''Scientific calculator implementing advanced mathematical operations.'''
    
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        return np.power(base, exponent)

    def sqrt(self, value: float) -> float:
        if value < 0:
            raise ValueError("Cannot compute square root of negative number.")
        return np.sqrt(value)

    def log(self, value: float, base: float = np.e) -> float:
        if value <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
            # natural log as foundation, change-of-base formula
        return np.log(value) / np.log(base)
    
    